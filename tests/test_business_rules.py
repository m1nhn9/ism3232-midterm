from business_rules import (
    calculate_room_cost,
    calculate_stay_total,
    format_stay_line,
    get_stay_discount,
    gets_welcome_package,
    requires_credit_check,
)


def test_room_cost_multiplies_rate_by_nights():
    assert round(calculate_room_cost(110.0, 2), 2) == 220.0


def test_room_cost_for_one_night():
    assert round(calculate_room_cost(125.5, 1), 2) == 125.5


def test_three_nights_has_no_discount():
    assert get_stay_discount(3) == 0.0


def test_four_nights_gets_six_percent_discount():
    assert get_stay_discount(4) == 0.06


def test_thirteen_nights_gets_six_percent_discount():
    assert get_stay_discount(13) == 0.06


def test_fourteen_nights_gets_eighteen_percent_discount():
    assert get_stay_discount(14) == 0.18


def test_corporate_changes_short_stay_discount():
    assert get_stay_discount(2, corporate=False) == 0.0
    assert get_stay_discount(2, corporate=True) == 0.06


def test_corporate_preserves_eighteen_percent_for_long_stay():
    assert get_stay_discount(14, corporate=True) == 0.18


def test_short_stay_total_includes_cleaning_fee():
    assert round(calculate_stay_total(110.0, 2), 2) == 260.0


def test_four_night_stay_total_applies_discount():
    assert round(calculate_stay_total(100.0, 4), 2) == 376.0


def test_cleaning_fee_applies_at_three_hundred_dollars():
    assert round(calculate_stay_total(300.0, 1), 2) == 340.0


def test_cleaning_fee_applies_just_below_limit():
    assert round(calculate_stay_total(299.99, 1), 2) == 339.99


def test_cleaning_fee_does_not_apply_just_above_limit():
    assert round(calculate_stay_total(300.01, 1), 2) == 300.01


def test_corporate_changes_short_stay_total():
    assert round(calculate_stay_total(150.0, 2, corporate=False), 2) == 340.0
    assert round(calculate_stay_total(150.0, 2, corporate=True), 2) == 322.0


def test_credit_check_not_required_just_below_two_thousand():
    assert requires_credit_check(1999.99) is False


def test_credit_check_required_at_two_thousand():
    assert requires_credit_check(2000.0) is True


def test_credit_check_required_just_above_two_thousand():
    assert requires_credit_check(2000.01) is True


def test_welcome_package_not_given_at_five_nights_with_qualifying_total():
    assert gets_welcome_package(5, 1000.0) is False


def test_welcome_package_given_at_six_nights_with_qualifying_total():
    assert gets_welcome_package(6, 1000.0) is True


def test_welcome_package_not_given_just_below_one_thousand_with_six_nights():
    assert gets_welcome_package(6, 999.99) is False


def test_welcome_package_given_at_one_thousand_with_ten_nights():
    assert gets_welcome_package(10, 1000.0) is True


def test_welcome_package_given_just_above_one_thousand_with_six_nights():
    assert gets_welcome_package(6, 1000.01) is True


def test_format_stay_line_shows_no_for_both_false_values():
    assert (
        format_stay_line("Kessler", 260.0, False, False)
        == "Kessler: $260.00 | credit check: no | welcome package: no"
    )


def test_format_stay_line_shows_yes_for_both_true_values():
    assert (
        format_stay_line("Nakata", 2296.0, True, True)
        == "Nakata: $2296.00 | credit check: yes | welcome package: yes"
    )


def test_format_stay_line_formats_mixed_flags_and_two_decimal_places():
    assert (
        format_stay_line("Quinn", 1015.2, False, True)
        == "Quinn: $1015.20 | credit check: no | welcome package: yes"
    )


def test_format_stay_line_formats_credit_check_without_welcome_package():
    assert (
        format_stay_line("Short stay", 2000.0, True, False)
        == "Short stay: $2000.00 | credit check: yes | welcome package: no"
    )
