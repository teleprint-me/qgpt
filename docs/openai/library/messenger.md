# OpenAI_Messenger

`OpenAI_Messenger` is a class for interacting with the OpenAI API to create text completions and chat completions. It handles API requests, rate limiting, and streaming.

## `__init__(self, api_key: Optional[str] = "") -> None`

Initialize an instance of `OpenAI_Messenger` with an optional API key.

- `api_key` (str, optional): OpenAI API key. If not provided, it will try to use the `OPENAI_API_KEY` environment variable.

### `query(self, endpoint: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]`

Send a query to the specified API endpoint with the given parameters.

- `endpoint` (str): API endpoint to call.
- `params` (dict, optional): Dictionary of parameters to pass to the endpoint.

Returns a dictionary containing the response from the API.

### `stream(self, params: Optional[dict] = None) -> Generator[Event, None, None]`

Stream events from the specified API endpoint.

- `params` (dict, optional): Dictionary of parameters to pass to the endpoint.

Yields `Event` objects as they are received from the API.

### `create_completion(self, ...) -> dict[str, Any]`

Create a text completion using the specified parameters.

Refer to the method signature and inline documentation for details on the available parameters.

Returns a dictionary containing the completion response from the API.

### `create_chat_completion(self, ...) -> dict[str, Any]`

Create a chat completion using the specified parameters.

Refer to the method signature and inline documentation for details on the available parameters.

Returns a dictionary containing the chat completion response from the API.

## Summary

The `OpenAI_Messenger` class provides an easy way to interact with the OpenAI API for text completions and chat completions. It handles API requests, rate limiting, and streaming. The main methods are `query`, `stream`, `create_completion`, and `create_chat_completion`.
