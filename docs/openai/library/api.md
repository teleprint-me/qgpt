# OpenAI_API

`OpenAI_API` is a class to manage OpenAI API information and construct request URLs and headers for API calls.

## `__init__(self, _api_key: str = os.getenv("OPENAI_API_KEY") or "", _org_id: str = os.getenv("OPENAI_ORGANIZATION_ID") or "")`

Initialize an instance of `OpenAI_API` with API key and organization ID.

- `_api_key` (str, optional): OpenAI API key. Defaults to the `OPENAI_API_KEY` environment variable.
- `_org_id` (str, optional): OpenAI organization ID. Defaults to the `OPENAI_ORGANIZATION_ID` environment variable.

### `api_key(self) -> str`

Get the API key.

Returns the API key as a string.

### `org_id(self) -> str`

Get the organization ID.

Returns the organization ID as a string.

### `base_url(self) -> str`

Get the base URL for the API.

Returns the base URL as a string.

### `sse_url(self) -> str`

Get the SSE URL for the API.

Returns the SSE URL as a string.

### `headers(self) -> dict[str, str]`

Get the headers for the API.

Returns a dictionary containing the headers for the API.

### `version(self) -> int`

Get the API version.

Returns the API version as an integer.

### `path(self, endpoint: str) -> str`

Construct the path for an API endpoint.

- `endpoint` (str): The API endpoint.

Returns the path as a string.

### `url(self, endpoint: str) -> str`

Construct the URL for an API endpoint.

- `endpoint` (str): The API endpoint.

Returns the URL as a string.

## Summary

The `OpenAI_API` class manages OpenAI API information, constructs request URLs and headers for API calls, and provides access to API key, organization ID, and version information. The main methods and properties include `api_key`, `org_id`, `base_url`, `sse_url`, `headers`, `version`, `path`, and `url`.
