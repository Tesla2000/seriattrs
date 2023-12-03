from datetime import datetime

from src.seriattrs.db_attrs_converter import db_attrs_converter


def structure_datetime(element: str, _) -> datetime:
    if isinstance(element, datetime):
        return element
    return datetime.fromtimestamp(float(element))


db_attrs_converter.register_structure_hook(datetime, structure_datetime)
