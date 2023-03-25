import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any


def read_json(filepath: Path) -> Any:
    with open(filepath, "r") as file:
        return json.load(file)


def write_json(filepath: Path, content) -> None:
    with open(filepath, "w") as f:
        json.dump(content, f)


def force_read_json(filepath: Path, content) -> Any:
    try:
        return read_json(filepath)
    except (FileNotFoundError, JSONDecodeError):
        write_json(filepath, content)
        return read_json(filepath)


def update_json(filepath: Path, content) -> None:
    with open(filepath, "a") as f:
        json.dump(content, f)
