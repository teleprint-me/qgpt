from typing import Any

from .messenger import OpenAI_Messenger


class OpenAI_Model(OpenAI_Messenger):
    def list(self) -> dict[str, Any]:
        return self.get("/models")

    def retrieve(self, model: str) -> dict[str, Any]:
        return self.get(f"/models/{model}")
