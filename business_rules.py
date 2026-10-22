NO_DISCOUNT = 0.0
STANDARD_DISCOUNT_MIN_NIGHTS = 4
EXTENDED_DISCOUNT_MIN_NIGHTS = 14
STANDARD_DISCOUNT = 0.06
EXTENDED_DISCOUNT = 0.18
CLEANING_FEE_LIMIT = 300.0
CLEANING_FEE = 40.0


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Return the room cost before discounts or fees."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate for the stay length and account type."""
    if nights >= EXTENDED_DISCOUNT_MIN_NIGHTS:
        return EXTENDED_DISCOUNT
    if nights >= STANDARD_DISCOUNT_MIN_NIGHTS or corporate:
        return STANDARD_DISCOUNT
    return NO_DISCOUNT


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Return the discounted room cost with any applicable cleaning fee."""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)
    total = room_cost * (1 - discount)
    if total <= CLEANING_FEE_LIMIT:
        total += CLEANING_FEE
    return total
