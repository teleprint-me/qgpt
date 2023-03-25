from PySide6.QtCore import Slot
from PySide6.QtGui import QFont, QTextCharFormat
from PySide6.QtWidgets import (
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from .thread import ResponseThread


class ChatWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()

        # Create a message queue to manage the chat history
        self.message_queue = main_window.message_queue
        # Attach the status bar method to the widget
        self.update_status_bar = main_window.update_status_bar
        self.update_status_bar_pending = main_window.update_status_bar_pending

        # Create a response thread
        self.response_thread = ResponseThread(self.message_queue)
        self.response_thread.response_generated.connect(self.handle_response)

        # Create assistant widgets
        self.chat_label = QLabel("Output:")
        self.input_label = QLabel("Input:")
        self.chat_history = QPlainTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.input_box = QTextEdit(self)
        self.send_button = QPushButton("Send", self)

        # Create chat column layout
        chat_column_layout = QVBoxLayout()
        chat_column_layout.addWidget(self.chat_label)
        chat_column_layout.addWidget(self.chat_history)
        chat_column_layout.addWidget(self.input_label)
        chat_column_layout.addWidget(self.input_box)
        chat_column_layout.addWidget(self.send_button)

        self.setLayout(chat_column_layout)

        # Connect buttons to corresponding functions
        self.send_button.clicked.connect(self.send_message)

        self.load_chat_history()

    def load_chat_history(self):
        self.chat_history.clear()
        for message in self.message_queue.history:
            role = message["role"]
            content = message["content"]

            cursor = self.chat_history.textCursor()
            format_bold = QTextCharFormat()
            format_bold.setFontWeight(QFont.Bold)
            format_normal = QTextCharFormat()
            format_normal.setFontWeight(QFont.Normal)

            cursor.insertText(f"{role.capitalize()}\n", format_bold)
            cursor.insertText(f"{content}\n\n", format_normal)
            self.chat_history.setTextCursor(cursor)

    def clear_chat_history(self):
        self.message_queue.clear()
        self.load_chat_history()

    def save_chat_history(self):
        self.message_queue.save()

    @Slot()
    def send_message(self):
        # Get the user's message from the input box
        message = self.input_box.toPlainText().strip()
        # Clear the input box
        self.input_box.clear()

        # Add the user's message to the chat history
        cursor = self.chat_history.textCursor()
        format_bold = QTextCharFormat()
        format_bold.setFontWeight(QFont.Bold)
        format_normal = QTextCharFormat()
        format_normal.setFontWeight(QFont.Normal)

        cursor.insertText("User\n", format_bold)
        cursor.insertText(f"{message}\n\n", format_normal)
        self.chat_history.setTextCursor(cursor)

        # Add user message to message queue
        self.message_queue.add_message("user", message)
        # Update the status bar to show "message pending"
        self.update_status_bar_pending()
        # Start the response thread
        self.response_thread.start()

    @Slot(str)
    def handle_response(self, response):
        # Add the assistant's response to the chat history
        cursor = self.chat_history.textCursor()
        format_bold = QTextCharFormat()
        format_bold.setFontWeight(QFont.Bold)
        format_normal = QTextCharFormat()
        format_normal.setFontWeight(QFont.Normal)

        cursor.insertText("Assistant\n", format_bold)
        cursor.insertText(f"{response}\n\n", format_normal)
        self.chat_history.setTextCursor(cursor)

        # Update the status bar to show "message complete"
        self.update_status_bar()
