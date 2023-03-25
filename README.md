# Q-GPT

Q-GPT is a powerful and user-friendly Graphical User Interface (GUI) built with Qt and PySide6, specifically designed for seamless interaction with OpenAI's GPT language models. It aims to provide an efficient and intuitive way to communicate with the AI, simplifying the experience for users and developers alike.

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

-   Ability to access relevant information from publicly available documentation, such as man pages, programming languages, APIs, etc. This feature requires careful planning and attention.

**Note**: This should be implemented after stabilizing memory and before introducing tooling.

#### Source Code

-   Ability to interact with source code, including AI and developer collaboration in the editor.

-   In-place text editing should be available by this stage.

-   Implementation depends on the stability and reliability of the assistant module.

#### Command Line Interface

-   Ability to interact with the command-line interface, with AI and developer collaboration.

-   In-place text editing should be available by this stage.

-   Implementation depends on the stability and reliability of both the assistant and editor modules.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/your_username/q-gpt.git
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the application:

```sh
python qgpt
```

## License

This project is licensed under the [LGPL License](https://github.com/teleprint-me/qgpt/blob/main/LICENSE).

## Contributing

If you would like to contribute to the development of Q-GPT, please submit a pull request or create an issue on the GitHub repository.
