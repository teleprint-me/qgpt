import sys

from assistant import MessageQueue, ResponseThread
from gui import MenuBar
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont, QTextCharFormat
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Q_GPT(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q-GPT")
        self.setGeometry(200, 200, 500, 500)

        # Create a message queue to manage the chat history
        self.message_queue = MessageQueue()
        # Create a response thread
        self.response_thread = ResponseThread(self.message_queue)
        self.response_thread.response_generated.connect(self.handle_response)

        # Create menu bar
        menu_bar = MenuBar()
        self.setMenuBar(menu_bar)

        #
        # Chat (Left) Column: Create assistant widgets
        #
        self.chat_label = QLabel("Chat:")
        self.chat_history = QPlainTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.input_box = QTextEdit(self)
        self.send_button = QPushButton("Send", self)

        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)
        # Create chat column layout
        chat_column_layout = QVBoxLayout()
        chat_column_layout.addWidget(self.chat_history)
        chat_column_layout.addWidget(self.input_box)
        chat_column_layout.addLayout(button_layout)

        #
        # Editor (Right) Column: Create developer widgets
        #

        # Create developer column label
        self.text_label = QLabel("Editor:")

        # Create the text editor
        self.text_editor = QPlainTextEdit()

        # Create editor layout
        dev_column_layout = QVBoxLayout()
        dev_column_layout.addWidget(self.text_editor)

        #
        # Chat-Editor hybrid interface layout
        #
        main_layout = QHBoxLayout()
        main_layout.addLayout(chat_column_layout)
        main_layout.addLayout(dev_column_layout)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to corresponding functions
        self.send_button.clicked.connect(self.send_message)

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.update_status_bar()
        self.load_chat_history()

    def update_status_bar(self):
        self.statusBar.clearMessage()
        count = str(self.message_queue.token_count)
        assistant = self.message_queue.assistant.capitalize()
        max = self.message_queue.max_tokens
        self.statusBar.showMessage(
            f"Role: {assistant} | Max Tokens: {max} | Total Tokens: {count}"
        )

    def update_status_bar_pending(self):
        self.statusBar.clearMessage()
        assistant = self.message_queue.assistant.capitalize()
        self.statusBar.showMessage(
            f"{assistant} is processing your request..."
        )

    def clear_chat_history(self):
        self.message_queue.clear()
        self.chat_history.clear()
        self.update_status_bar()
        self.load_chat_history()

    def save_chat_history(self):
        self.message_queue.save()

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

    @Slot()
    def show_about_dialog(self):
        QMessageBox.information(
            self,
            "About",
            "Q-GPT is a QT GUI Toolkit that integrates GPT models as first-class components in the application. It provides an easy way to create GUI applications that interact with GPT models, enabling seamless communication and response handling.",
        )

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

    def closeEvent(self, event):
        # Save the queue state before exiting
        self.message_queue.save()
        # Exit program
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Q_GPT()
    window.show()
    sys.exit(app.exec())
