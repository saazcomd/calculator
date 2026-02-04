"""Simple expression calculator with safe parsing."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Union


Number = Union[int, float]


class CalculatorError(ValueError):
    """Raised when an invalid expression is provided."""


@dataclass(frozen=True)
class CalculationResult:
    expression: str
    value: Number


class _Evaluator(ast.NodeVisitor):
    def visit_Expression(self, node: ast.Expression) -> Number:  # noqa: N802
        return self.visit(node.body)

    def visit_BinOp(self, node: ast.BinOp) -> Number:  # noqa: N802
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise CalculatorError("Division by zero is not allowed.")
            return left / right
        if isinstance(node.op, ast.Pow):
            return left**right

        raise CalculatorError(f"Unsupported operator: {ast.dump(node.op)}")

    def visit_UnaryOp(self, node: ast.UnaryOp) -> Number:  # noqa: N802
        operand = self.visit(node.operand)

        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand

        raise CalculatorError(f"Unsupported unary operator: {ast.dump(node.op)}")

    def visit_Num(self, node: ast.Num) -> Number:  # noqa: N802
        return node.n

    def visit_Constant(self, node: ast.Constant) -> Number:  # noqa: N802
        if isinstance(node.value, (int, float)):
            return node.value
        raise CalculatorError("Only numeric constants are allowed.")

    def generic_visit(self, node: ast.AST) -> Number:
        raise CalculatorError(f"Unsupported expression: {ast.dump(node)}")


def evaluate_expression(expression: str) -> CalculationResult:
    """Evaluate a math expression and return a CalculationResult."""
    if not expression or not expression.strip():
        raise CalculatorError("Expression cannot be empty.")

    try:
        parsed = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise CalculatorError("Invalid expression syntax.") from exc

    value = _Evaluator().visit(parsed)
    return CalculationResult(expression=expression, value=value)


__all__ = ["CalculatorError", "CalculationResult", "evaluate_expression"]
