from pathlib import Path
from typing import Optional

from assistant.setting import (
    AssistantPath,
    AssistantSetting,
    force_read_json,
    get_assistant_path,
    write_json,
)


class AssistantMemory(AssistantSetting):
    def __init__(self, assistant_path: Optional[AssistantPath] = None):
        self._path = get_assistant_path(assistant_path)
        self._dataset: dict[str, str] = {}
        self.load()

    @property
    def filepath(self) -> Path:
        return self._path.memory

    @property
    def memories(self) -> dict[str, str]:
        return self._dataset

    def clear(self) -> None:
        self._dataset = {}

    def save(self) -> None:
        write_json(self.filepath, self._dataset)

    def load(self) -> None:
        self._dataset = force_read_json(self.filepath, self._dataset)
