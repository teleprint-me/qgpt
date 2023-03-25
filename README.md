# Q-GPT

Q-GPT aims to be a user-friendly Graphical User Interface (GUI) built with Qt and PySide6 for seamless interaction with OpenAI's GPT language models. The goal is to provide an efficient and intuitive way to communicate with the AI, simplifying the experience for users and developers.

**Note**: Q-GPT is currently a Work In Progress (WIP). Working prototypes will be made available through tagged releases.

## Prototyped Features

- Custom OpenAI REST API interface for seamless GPT model interaction
- Context management system:
  - Records conversation context, history, and completions
  - Plans to implement a buffer system
  - Threaded message queues for a smooth user experience
- Chat interface components:
  - Chat Box: Displays conversation between user and assistant
  - Input Box: Collects user input
  - Send Button: Submits user input to the assistant
- Provisional editor interface with plans for a feature-rich text editor in later stages

## Installation and Usage

1. **Clone the repository:**

```sh
git clone https://github.com/teleprint-me/qgpt.git
cd qgpt
```

2. **Install Poetry (optional):**

Poetry is the preferred method for managing Python packages. If you don't have Poetry installed, you can install it using pipx.

```sh
pip install --user --upgrade pipx
pipx install poetry
```

To update Poetry, run:

```sh
pipx upgrade poetry
```

3. **Install Python packages:**

- Using Poetry:

```sh
poetry install
poetry shell
```

- Using venv and `requirements.txt`:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

4. **Run the application:**

```sh
python qgpt
```

## License

This project is licensed under the [LGPL License](https://github.com/teleprint-me/qgpt/blob/main/LICENSE).

## Contributing

If you would like to contribute to the development of Q-GPT, please submit a pull request or create an issue on the GitHub repository.
