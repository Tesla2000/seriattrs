from decimal import Decimal

from src.seriattrs.db_attrs_converter import db_attrs_converter


def structure_decimal(element: str, _) -> Decimal:
    if isinstance(element, Decimal):
        return element
    return Decimal(element)


db_attrs_converter.register_structure_hook(Decimal, structure_decimal)
