import sys

from assistant import MessageQueue, ResponseThread
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QFont, QTextCharFormat
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QWidget,
)


class Q_GPT(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q-GPT")
        self.setGeometry(200, 200, 500, 500)

        # Create menu bar
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu("File")
        help_menu = menu_bar.addMenu("Help")

        # Add actions to the File menu
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        file_menu.addAction(exit_action)

        # Add actions to the Help menu
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

        # Create the input box
        self.input_box = QTextEdit(self)

        # Create the chat history box
        self.chat_history = QPlainTextEdit(self)
        self.chat_history.setReadOnly(True)

        # Create buttons
        self.clear_button = QPushButton("Clear", self)
        self.save_button = QPushButton("Save", self)
        self.load_button = QPushButton("Load", self)
        self.send_button = QPushButton("Send", self)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.send_button)

        # Create a grid layout
        grid_layout = QGridLayout()

        # Add input box and chat history box to the grid layout
        grid_layout.addWidget(self.chat_history, 0, 0)
        grid_layout.addWidget(self.input_box, 0, 1)

        # Add button container to the grid layout
        grid_layout.addLayout(button_layout, 1, 0, 1, 2)

        # Create a central widget and set the grid layout
        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to corresponding functions
        self.clear_button.clicked.connect(self.clear_chat_history)
        self.save_button.clicked.connect(self.save_chat_history)
        self.load_button.clicked.connect(self.load_chat_history)
        self.send_button.clicked.connect(self.send_message)

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Create a message queue to manage the chat history
        self.message_queue = MessageQueue()

        # Create a response thread
        self.response_thread = ResponseThread(self.message_queue)
        self.response_thread.response_generated.connect(self.handle_response)

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

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Q_GPT()
    window.show()
    sys.exit(app.exec())
