import sys

from PySide6.QtCore import Slot
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


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT GPT Toolkit")
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

    @Slot()
    def send_message(self):
        message = self.input_box.text()
        self.chat_history.appendPlainText("You: " + message)
        self.input_box.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
