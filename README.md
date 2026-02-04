# Calculator

A simple, safe calculator that evaluates arithmetic expressions from the command line.

## Features
- Supports addition, subtraction, multiplication, division, and exponentiation.
- Handles parentheses and unary operators.
- Rejects unsafe or unsupported expressions.

## Usage

```bash
python src/main.py "3 + 4 * 2"
```

Example output:

```text
3 + 4 * 2 = 11
```

To enter an expression interactively, omit the argument:

```bash
python src/main.py
```
