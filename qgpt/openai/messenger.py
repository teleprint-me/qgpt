import time
from typing import Any, Generator, Optional

import requests
from openai.api import OpenAI_API, get_api_key
from requests.exceptions import HTTPError
from sseclient import Event, SSEClient


class OpenAI_Messenger:
    def __init__(self, api_key: Optional[str] = "") -> None:
        self.api = OpenAI_API(get_api_key(api_key))
        self.session = requests.Session()

    def post(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        if not params:
            params = {}
        url = self.api.url(endpoint)
        headers = self.api.headers
        response = self.session.post(url, headers=headers, json=params)
        # rate limit error
        if response.status_code == 429:
            # retry with exponential back-off
            for i in range(5):
                delay = 2**i
                print(f"Retry {i + 1} in {delay} seconds...")
                time.sleep(delay)
                try:
                    response = self.session.post(
                        url, headers=headers, json=params
                    )
                    response.raise_for_status()
                    break
                except HTTPError as e:
                    print(f"Retry failed: {e}")
        else:
            response.raise_for_status()
        return response.json()

    def get(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        url = self.api.url(endpoint)
        headers = self.api.headers
        response = self.session.get(url, headers=headers, params=params)
        # rate limit error
        if response.status_code == 429:
            # retry with exponential back-off
            for i in range(5):
                delay = 2**i
                print(f"Retry {i + 1} in {delay} seconds...")
                time.sleep(delay)
                try:
                    response = self.session.get(
                        url, headers=headers, params=params
                    )
                    response.raise_for_status()
                    break
                except HTTPError as e:
                    print(f"Retry failed: {e}")
        else:
            response.raise_for_status()
        return response.json()

    def stream(
        self, params: Optional[dict] = None
    ) -> Generator[Event, None, None]:
        if not params:
            params = {}
        url = f'{self.api.sse_url}/{params["type"]}'
        headers = self.api.headers
        messages = SSEClient(url, headers=headers)
        for msg in messages:
            yield msg
