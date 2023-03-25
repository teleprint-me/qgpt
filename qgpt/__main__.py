import sys

from assistant import MessageQueue
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q-GPT")
        self.setGeometry(200, 200, 500, 500)

        # Add the file menu bar
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Create menu bar exit option
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        # Add exit option to menu bar
        self.file_menu.addAction(exit_action)

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

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Create a message queue to manage the chat history
        self.message_queue = MessageQueue()

        self.update_status_bar()

        self.display_message_history()

    def display_message_history(self):
        for message in self.message_queue.history:
            role = message["role"]
            content = message["content"]
            self.chat_history.appendPlainText(
                f"{role.capitalize()}: {content}\n"
            )

    def update_status_bar(self):
        count = str(self.message_queue.token_count)
        name = self.message_queue.assistant.capitalize()
        self.statusBar.showMessage(f"{name} is using {count} tokens")

    @Slot()
    def send_message(self):
        # Get the user's message from the input box
        message = self.input_box.text()
        # Clear the input box
        self.input_box.clear()
        # Add the user's message to the chat history
        self.chat_history.appendPlainText(f"User: {message}\n")
        # Add user message to message queue
        self.message_queue.add_message("user", message)
        # Generate a response from the assistant
        response = self.message_queue.generate_completion()
        # Add the assistant's response to the chat history
        self.chat_history.appendPlainText(f"Assistant: {response}\n")
        # Update the status bar
        self.update_status_bar()

    def closeEvent(self, event):
        # Save the queue state before exiting
        self.message_queue.save()
        # Exit program
        event.accept()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
