# ISM3232 Midterm: Seabreeze Inn

- **Name:** Minh Nguyen
- **Version:** DELTA
- **Date:** October 21, 2026

## What This Program Does

This program calculates the final price of eight stays at Seabreeze Inn and shows which guests need a credit check or receive a welcome package. It displays each guest's result, then summarizes the number of stays, reserved revenue, average total, largest stay, credit checks, and welcome packages. The pricing rules are separate from the report so they can be tested independently.

## Business Rules

1. Multiply the nightly rate by the number of nights to find the room cost.
2. Apply no discount for fewer than 4 nights, 6% for 4 through 13 nights, and 18% for 14 nights or more.
3. Give corporate-account guests at least 6% off, including on short stays; longer stays still receive the 18% rate.
4. Add a $40 cleaning fee when the room cost after the discount is $300 or less.
5. Require a credit check when the final stay total reaches $2,000.
6. Provide a welcome package when the stay lasts more than 5 nights and its final total is at least $1,000.

## How to Run

Use Python 3 in a terminal opened in this repository. These commands work on macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

With the virtual environment active, run:

```sh
ruff format .
ruff format --check .
ruff check .
pytest -v
```

The project has 34 tests covering all eight functions, the six rule boundaries, corporate discounts, and largest-stay ties and empty input. Run the formatting, lint, and test commands before every push.

## Files in This Repository

- `business_rules.py`: The eight typed functions and the constants used by the business rules.
- `main.py`: The eight example stays, the report it prints, and the summary counts.
- `commands.md`: The recorded setup and verification commands, their captured outputs, and the limits of the available setup record.
- `README.md`: Project information, business rules, and run and test instructions.
- `requirements.txt`: Installed tool versions captured with pip freeze.
- `.gitignore`: Excludes the virtual environment, Python bytecode, and tool caches.
- `tests/__init__.py`: Marks the tests directory as a Python package.
- `tests/test_business_rules.py`: The 34 pytest tests for the business functions.

## AI Use Statement

No AI interaction was used for this project
