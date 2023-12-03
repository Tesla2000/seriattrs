from importlib import import_module
from pathlib import Path

tuple(
    import_module('.' + module.name.partition(".")[0], __package__)
    for module in Path(__file__).parent.iterdir()
    if module.name not in ("__init__.py", "pycache")
)
