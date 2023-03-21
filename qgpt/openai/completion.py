from typing import Any, Optional

from openai.messenger import OpenAI_Messenger


class OpenAI_Completion(OpenAI_Messenger):
    def completions(
        self,
        prompt: str | list[str],
        model: Optional[str] = "text-davinci-003",
        max_tokens: Optional[int] = 256,
        temperature: Optional[float] = 1,
        **params
    ) -> dict[str, Any]:
        keys = ["prompt", "model", "max_tokens", "temperature"]
        values = [prompt, model, max_tokens, temperature]
        for key, value in zip(keys, values):
            params[key] = value
        return self.post("/completions", params=params)

    def chat_completions(
        self,
        messages: list[dict[str, str]],
        model: Optional[str] = "gpt-3.5-turbo",
        max_tokens: Optional[int] = 256,
        temperature: Optional[float] = 0.5,
        **params
    ) -> dict[str, Any]:
        keys = ["messages", "model", "max_tokens", "temperature"]
        values = [messages, model, max_tokens, temperature]
        for key, value in zip(keys, values):
            params[key] = value
        return self.post("/chat/completions", params=params)
