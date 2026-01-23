from decimal import Decimal, ROUND_HALF_UP


def round_money(value: Decimal | float) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
