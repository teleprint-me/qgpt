from typing import Optional

from .api import get_api_key
from .completion import OpenAI_Completion
from .messenger import OpenAI_Messenger
from .model import OpenAI_Model


class OpenAI:
    def __init__(self, api_key: Optional[str] = "") -> None:
        api_key = get_api_key(api_key)

        self.messenger = OpenAI_Messenger(api_key)
        self.completion = OpenAI_Completion(api_key)
        self.model = OpenAI_Model(api_key)
