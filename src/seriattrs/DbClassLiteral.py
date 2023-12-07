from typing import get_args

from attr import fields
from attrs import define

from .DbClass import DbClass
from .db_attrs_converter import db_attrs_converter


@define
class DbClassLiteral(DbClass):
    pass


def _handle_new_db(value, db_class_type):
    if isinstance(value, int):
        return value
    id_value = value.pop("_id")
    new_instance = db_class_type(**value)
    new_instance._id = id_value
    value["_id"] = id_value
    for f in fields(db_class_type):
        types = list(get_args(f.type))
        if isinstance(f.type, type):
            types.append(f.type)
        if references := tuple(field_type for field_type in types if isinstance(field_type, str)):
            raise ValueError(f"Data can't be deserialized as field {f.name} in {db_class_type.__name__} has a forward references {references}. Consider making classes {references} DbClasses and initializing them.")
        if any(issubclass(field_type, DbClassLiteral) for field_type in types):
            setattr(
                new_instance,
                f.name,
                db_attrs_converter.structure(value[f.name], f.type),
            )
    return new_instance


db_attrs_converter.register_structure_hook_func(
    lambda t: issubclass(t, DbClass), _handle_new_db
)