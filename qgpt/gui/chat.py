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


class ChatWidget(QWidget):
    def __init__(self, message_queue, handle_send_message):
        super().__init__()

        # Set the message queue and send message handler
        self.message_queue = message_queue
        self.handle_send_message = handle_send_message

        # Create assistant widgets
        self.chat_label = QLabel("Chat:")
        self.chat_history = QPlainTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.input_box = QTextEdit(self)
        self.send_button = QPushButton("Send", self)

        # Create chat column layout
        chat_column_layout = QVBoxLayout()
        chat_column_layout.addWidget(self.chat_history)
        chat_column_layout.addWidget(self.input_box)
        chat_column_layout.addWidget(self.send_button)

        self.setLayout(chat_column_layout)

        # Connect buttons to corresponding functions
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        self.handle_send_message(self.input_box.toPlainText().strip())
        self.input_box.clear()
