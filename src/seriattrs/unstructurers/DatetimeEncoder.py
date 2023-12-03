from datetime import datetime

from src.seriattrs.db_attrs_converter import db_attrs_converter

db_attrs_converter.register_unstructure_hook(datetime, datetime.timestamp)
