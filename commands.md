# Terminal Record: Seabreeze Inn

## 1. Building the project

This workspace already contained the project folder, the original seven files, the GitHub remote, and two commits when this session began. The earlier folder creation, empty-file creation, initial virtual environment, .gitignore creation, and GitHub connection commands were not available, so they cannot be reproduced as an original terminal record. The existing repository was continued without replacing its history.

These are the setup commands actually executed in this session, in order:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
touch commands.md
```

The Python files, tests, README, and additional cache exclusions were edited using Codex's patch tool. The requirements file above came from the newly created virtual environment. The following sections contain terminal output captured during this session.

## 2. The virtual environment

The virtual environment was activated before running this command.

```sh
which python3
```

```text
/Users/hoo/conductor/workspaces/ism3232-midterm/sydney/.venv/bin/python3
```

The path ends in this workspace's .venv/bin/python3, showing that the active Python interpreter belongs to the virtual environment.

## 3. The project structure

```sh
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The .venv folder exists on this computer but is excluded from GitHub by .gitignore because it holds the locally installed interpreter and packages.

## 4. Every function and test

```sh
rg 'def '
```

```text
business_rules.py:def calculate_room_cost(nightly_rate: float, nights: int) -> float:
business_rules.py:def get_stay_discount(nights: int, corporate: bool = False) -> float:
business_rules.py:def calculate_stay_total(
business_rules.py:def requires_credit_check(total: float) -> bool:
business_rules.py:def gets_welcome_package(nights: int, total: float) -> bool:
business_rules.py:def total_reserved(stays: list) -> float:
business_rules.py:def largest_stay(stays: list) -> str:
business_rules.py:def format_stay_line(
tests/test_business_rules.py:def test_room_cost_multiplies_rate_by_nights():
tests/test_business_rules.py:def test_room_cost_for_one_night():
tests/test_business_rules.py:def test_three_nights_has_no_discount():
tests/test_business_rules.py:def test_four_nights_gets_six_percent_discount():
tests/test_business_rules.py:def test_thirteen_nights_gets_six_percent_discount():
tests/test_business_rules.py:def test_fourteen_nights_gets_eighteen_percent_discount():
tests/test_business_rules.py:def test_corporate_changes_short_stay_discount():
tests/test_business_rules.py:def test_corporate_preserves_eighteen_percent_for_long_stay():
tests/test_business_rules.py:def test_short_stay_total_includes_cleaning_fee():
tests/test_business_rules.py:def test_four_night_stay_total_applies_discount():
tests/test_business_rules.py:def test_cleaning_fee_applies_at_three_hundred_dollars():
tests/test_business_rules.py:def test_cleaning_fee_applies_just_below_limit():
tests/test_business_rules.py:def test_cleaning_fee_does_not_apply_just_above_limit():
tests/test_business_rules.py:def test_corporate_changes_short_stay_total():
tests/test_business_rules.py:def test_credit_check_not_required_just_below_two_thousand():
tests/test_business_rules.py:def test_credit_check_required_at_two_thousand():
tests/test_business_rules.py:def test_credit_check_required_just_above_two_thousand():
tests/test_business_rules.py:def test_welcome_package_not_given_at_five_nights_with_qualifying_total():
tests/test_business_rules.py:def test_welcome_package_given_at_six_nights_with_qualifying_total():
tests/test_business_rules.py:def test_welcome_package_not_given_just_below_one_thousand_with_six_nights():
tests/test_business_rules.py:def test_welcome_package_given_at_one_thousand_with_ten_nights():
tests/test_business_rules.py:def test_welcome_package_given_just_above_one_thousand_with_six_nights():
tests/test_business_rules.py:def test_format_stay_line_shows_no_for_both_false_values():
tests/test_business_rules.py:def test_format_stay_line_shows_yes_for_both_true_values():
tests/test_business_rules.py:def test_format_stay_line_formats_mixed_flags_and_two_decimal_places():
tests/test_business_rules.py:def test_format_stay_line_formats_credit_check_without_welcome_package():
tests/test_business_rules.py:def test_total_reserved_adds_stays_with_discounts_and_cleaning_fees():
tests/test_business_rules.py:def test_total_reserved_returns_zero_for_empty_list():
tests/test_business_rules.py:def test_total_reserved_handles_one_stay():
tests/test_business_rules.py:def test_largest_stay_uses_total_instead_of_nightly_rate():
tests/test_business_rules.py:def test_largest_stay_keeps_first_guest_when_totals_tie():
tests/test_business_rules.py:def test_largest_stay_returns_empty_string_for_empty_list():
tests/test_business_rules.py:def test_largest_stay_uses_corporate_discount():
tests/test_business_rules.py:def test_largest_stay_includes_cleaning_fee_in_comparison():
commands.md:rg 'def '
```

The business_rules.py file defines 8 functions, and tests/test_business_rules.py defines 34 tests; matches in Markdown files are not included in those counts.

## 5. Which files print

```sh
rg -l 'print'
```

```text
main.py
README.md
commands.md
```

The Python file main.py prints the report; business_rules.py is absent because its functions return values without producing console output.

## 6. The commit history

```sh
git log --oneline
```

```text
9581569 Document Seabreeze Inn rules, usage, tests, and AI assistance
520d66f Print the Seabreeze Inn stay report and loop-counted summaries
8b3be0a Implement loop-based reservation totals and largest-stay selection with tests
a7eddef Add credit checks, welcome packages, and stay-line formatting with tests
5d39485 Implement room pricing, stay discounts, and cleaning fees with tests
5c35eed Add README title, run, and test sections
98097f2 Set up project structure and gitignore
```

There were 7 commits when this history was captured, immediately before committing this terminal record.
