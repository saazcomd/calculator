import pytest

from calculator import CalculatorError, evaluate_expression


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("1 + 2", 3),
        ("5 - 3", 2),
        ("2 * 3", 6),
        ("8 / 4", 2),
        ("2 ** 3", 8),
        ("-(4 + 1)", -5),
    ],
)
def test_evaluate_expression(expression, expected):
    result = evaluate_expression(expression)
    assert result.value == expected


def test_division_by_zero():
    with pytest.raises(CalculatorError):
        evaluate_expression("10 / 0")


def test_invalid_expression():
    with pytest.raises(CalculatorError):
        evaluate_expression("import os")
