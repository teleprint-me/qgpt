# Q-GPT

Q-GPT is (going to be) a powerful and user-friendly (hopefully) Graphical User Interface (GUI) built with Qt and PySide6 (definitely), specifically designed for seamless interaction with OpenAI's GPT language models (fingers crossed). It aims to provide an efficient and intuitive way to communicate with the AI (yes), simplifying the experience for users and developers alike (I like the thought of this, at least).

**Note**: Q-GPT is currently a Work In Progress (WIP). As the project progresses, working prototypes will be made available through tagged releases.

## Prototyped Features

-   Custom OpenAI REST API interface using a lightweight wrapper for seamless interaction with GPT models

-   Advanced context management system:

    -   Records conversation context, history, and completions
    -   Treats the conversation as a queue, with plans to implement a buffer system
    -   Threaded message queues to prevent interface freezing and ensure a smooth user experience

-   Chat interface, consisting of:

    -   Chat Box: Displays the entire conversation between the user and the assistant
    -   Input Box: Collects user input
    -   Send Button: Submits user input to the assistant

-   Provisional editor interface, with plans for a feature-rich text editor in later stages

## Roadmap

### Overview

The primary focus of Q-GPT's development is to create a robust and modular support structure, capable of accommodating various models and their architectures. The aim is to deliver a simple, powerful, and flexible user interface that simplifies interaction with GPT models and appeals to developers of all levels.

Q-GPT's core concept revolves around two main interfaces: the Chat and Editor interfaces. Both interfaces will be event-driven, enabling seamless collaboration between the AI and the developer or creator, using GPT or other models.

The ultimate goal is to minimize the barrier between the user and the assistant, enhancing the overall experience.

#### Model Support

-   Primary focus on supporting OpenAI GPT-based models for now, with plans to expand support for the full API over time.

-   Future plans to support various forks and spin-offs of the Llama model (such as dalai, alpaca, and more). This will enable users to work with their own personal models, with ongoing efforts to accommodate them as the project progresses.

#### Context Management

-   The `assistant` package is designed to handle message context, which can be treated as a buffer, queue, or stream.

    -   Each message within a conversation is represented as a dictionary.
    -   Each conversation is represented as a list of messages.
    -   JSON can be used to capture the conversation history, message context, and completions.
    -   Additional factors like settings and system prompts will also need to be taken into account.

-   Conversation state is saved automatically, with options to clear and load saved states.

-   Multi-context support is in planning. This would allow users to manage multiple conversations with various models.
    -   A possible approach is to map each context to its own working directory.

**Note**: Streams have not been implemented yet, and buffers are under development.

#### Command Prompting

-   Both the user and the assistant can issue and receive commands, enabling the execution of prompts and more intuitive interactions.

-   The AI and the user can work together effectively using these command prompts, as demonstrated in the `docs/frames/riley.md` example.

-   In the example conversation, Riley successfully executed commands like `@help`, `@memory create test_memory "This is a test memory created by Riley."`, and `@help @memory`, showcasing the practical application of command prompting.

**Note**: A sample conversation demonstrating command prompting can be found in the `docs/frames/riley.md` file.

#### Memory

-   The `assistant` package supports memory management through nested dictionaries, allowing the creation, reading, updating, and deletion of memory entries.

-   Each memory entry consists of unique nested keys and values, stored in a JSON file for the bot to utilize.

-   The prototype system, as demonstrated in the `docs/frames/riley.md` file, provides an example of a unidimensional memory management implementation.

-   Future developments will focus on expanding memory capabilities, such as handling multiple memories simultaneously, implementing more sophisticated memory retrieval mechanisms, and enhancing the nested dictionary structure.

**Note**: A sample conversation demonstrating the prototype memory management system can be found in the `docs/frames/riley.md` file.

#### Access to Documentation

-   Q-GPT aims to enable users and the AI assistant to access relevant information from publicly available documentation, such as man pages, programming languages, APIs, etc.

-   This feature requires careful planning and attention to ensure that the AI can understand and utilize the documentation effectively.

-   To implement this feature, integration with external resources and APIs may be necessary.

-   The development timeline for this feature is after stabilizing memory management and before introducing tooling and source code interaction capabilities.

**Note**: The implementation of this feature will depend on the stability and reliability of the memory management system, as well as the availability of suitable resources for documentation access.

#### Text Editor

-   Q-GPT aims to provide a feature-rich text editor that enables seamless interaction with source code, allowing both the AI assistant and the user to collaborate effectively.
-   The text editor will support various programming languages and file types, offering syntax highlighting, autocompletion, and other useful features to improve the overall user experience.
-   In-place text editing will be available within the text editor, allowing users to make modifications directly within the Q-GPT interface.
-   The development and implementation of the text editor will depend on the stability and reliability of the assistant module, as well as the availability of suitable resources for integration and customization.

**Note**: The text editor will be designed with the goal of enhancing collaboration between the user and the AI assistant, making it easier to work with source code and develop software projects.

#### Command Line Interface (CLI)

-   Q-GPT will include a built-in Command Line Interface (CLI) to provide users with a seamless and powerful way to interact with their operating system and other command-line tools.
-   The CLI will be designed for efficient collaboration between the AI assistant and the user, allowing them to work together on various tasks, such as running scripts, managing files, and executing commands.
-   In-place text editing will be available within the CLI, allowing users to make modifications directly within the Q-GPT interface.
-   The development and implementation of the CLI will depend on the stability and reliability of both the assistant and editor modules, as well as the availability of suitable resources for integration and customization.

**Note**: The CLI aims to enhance the user experience by providing an intuitive interface for AI-assisted command-line interactions, ultimately simplifying various tasks and improving overall productivity.

## Installation and Usage

1. Clone the repository:

```sh
git clone https://github.com/teleprint-me/qgpt.git
cd qgpt
```

2. Set up a Python virtual environment using your preferred tool (e.g., `venv` or `poetry`).

-   For `venv`:

```sh
python -m venv .venv
source .venv/bin/activate
```

-   For `poetry`:

```sh
pip install --user --upgrade pipx
pipx install poetry
poetry install
poetry shell
```

3. Install the required Python packages:

```sh
python -m pip install -U pip
python -m pip install -r requirements.txt
```

4. Run the application:

```sh
python qgpt
```

## License

This project is licensed under the [LGPL License](https://github.com/teleprint-me/qgpt/blob/main/LICENSE).

## Contributing

If you would like to contribute to the development of Q-GPT, please submit a pull request or create an issue on the GitHub repository.
