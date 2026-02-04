"""CLI entrypoint for the calculator."""

from __future__ import annotations

import argparse
import sys

from calculator import CalculatorError, evaluate_expression


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument(
        "expression",
        nargs="?",
        help="Expression to evaluate, e.g. '3 + 4 * 2'",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    expression = args.expression
    if expression is None:
        expression = input("Enter an expression: ")

    try:
        result = evaluate_expression(expression)
    except CalculatorError as exc:
        print(f"Error: {exc}")
        return 1

    print(f"{result.expression} = {result.value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
