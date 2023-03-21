import datetime
import shutil
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Optional

from .json import force_read_json, read_json, update_json, write_json
from .path import DEFAULT_SETTING, AssistantPath, get_assistant_path


class AssistantSetting:
    def __init__(self, assistant_path: Optional[AssistantPath] = None):
        self._path = get_assistant_path(assistant_path)
        self._dataset = DEFAULT_SETTING
        self.load()

    @property
    def filepath(self) -> Path:
        return self._path.setting

    @property
    def keys(self) -> list[str]:
        return list(self._dataset.keys())

    @property
    def settings(self) -> dict[str, Any]:
        return self._dataset

    def create(self, key: str, value: Any) -> bool:
        if key not in self._dataset:
            self._dataset[key] = value
            return True
        else:
            return False

    def create_nested(self, value: Any, *keys: str) -> bool:
        setting = self._dataset
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if isinstance(setting, dict):
                setting = setting.setdefault(key, {})
            else:
                return False

        if last_key not in setting:
            setting[last_key] = value
            return True
        else:
            return False

    def read(self, key: str) -> Any:
        return self._dataset.get(key, None)

    def read_nested(self, *keys: str) -> Any:
        setting = self._dataset
        for key in keys:
            if isinstance(setting, dict) and key in setting:
                setting = setting.get(key, None)
            else:
                return None
        return setting

    def update(self, key: str, value: Any) -> bool:
        if key in self._dataset:
            self._dataset[key] = value
            return True
        else:
            return self.create(key, value)

    def update_nested(self, value: Any, *keys: str) -> bool:
        setting = self._dataset
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if isinstance(setting, dict) and key in setting:
                setting = setting[key]
            else:
                return False

        if isinstance(setting, dict) and last_key in setting:
            setting[last_key] = value
            return True
        else:
            return self.create_nested(value, *keys)

    def delete(self, key: str) -> bool:
        if key in self._dataset:
            del self._dataset[key]
            return True
        else:
            return False

    def delete_nested(self, *keys: str) -> bool:
        setting = self._dataset
        last_key = keys[-1]
        keys = keys[:-1]

        for key in keys:
            if isinstance(setting, dict) and key in setting:
                setting = setting[key]
            else:
                return False

        if isinstance(setting, dict) and last_key in setting:
            del setting[last_key]
            return True
        else:
            return False

    def save(self) -> None:
        write_json(self.filepath, self._dataset)

    def load(self) -> None:
        try:
            self._dataset = read_json(self.filepath)
        except JSONDecodeError:
            self._dataset = DEFAULT_SETTING
            write_json(self.filepath, DEFAULT_SETTING)

    def backup(self) -> None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.filepath.name.replace(".json", f"_{timestamp}.json")
        backup_filename = self.filepath.parent / filename
        shutil.copyfile(self.filepath, backup_filename)
