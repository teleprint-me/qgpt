from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from assistant.setting.json import read_json

DEFAULT_PATH = "model"

DEFAULT_SETTING_PATH: Path = Path(f"{DEFAULT_PATH}/setting.json")
DEFAULT_SETTING: dict[str, Any] = read_json(DEFAULT_SETTING_PATH)


@dataclass(frozen=True)
class AssistantPath:
    setting: Path = Path(DEFAULT_SETTING["local"]["setting"])
    completion: Path = Path(DEFAULT_SETTING["local"]["completion"])
    memory: Path = Path(DEFAULT_SETTING["local"]["memory"])
    message: Path = Path(DEFAULT_SETTING["local"]["message"])
    history: Path = Path(DEFAULT_SETTING["local"]["history"])
    ptk_history: Path = Path(DEFAULT_SETTING["local"]["ptk_history"])


def get_assistant_path(
    assistant_path: Optional[AssistantPath] = None,
) -> AssistantPath:
    return assistant_path if assistant_path else AssistantPath()
