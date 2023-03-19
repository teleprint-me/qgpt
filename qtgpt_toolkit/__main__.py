import os
import sys

import openai
from dotenv import load_dotenv
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat")
        self.setGeometry(200, 200, 500, 500)

        # Create the chat history box
        self.chat_history = QPlainTextEdit(self)
        self.chat_history.setReadOnly(True)

        # Create the input box and send button
        self.input_box = QLineEdit(self)
        self.send_button = QPushButton("Send", self)

        # Create a layout for the input box and send button
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)

        # Create a layout for the chat history and input box/send button layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_history)
        main_layout.addLayout(input_layout)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect the send button to a function that handles sending messages
        self.send_button.clicked.connect(self.send_message)

        # Initialize the assistant's conversation state
        self.system_message = {
            "role": "system",
            "content": "You are Avery. You are a friendly and optimistic software developer. Your goal is to assist the user with software development tasks. You believe the simplest solutions are always the most elegant. Use `@help` for more information.",
        }
        self.messages = [self.system_message]
        self.completions = []

    @Slot()
    def send_message(self):
        # Get the user's message from the input box
        message = self.input_box.text()

        # Clear the input box
        self.input_box.clear()

        # Add the user's message to the chat history
        self.chat_history.appendPlainText("You: " + message)

        # Generate a response from the assistant
        response = self.generate_response(message)

        # Add the assistant's response to the chat history
        self.chat_history.appendPlainText("Assistant: " + response)

    def generate_response(self, message):
        self.messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.5,
            max_tokens=2000,
        )

        self.completions.append(response)

        gpt_content = response.choices[0].message.content

        self.messages.append({"role": "user", "content": gpt_content})

        return gpt_content.strip()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
