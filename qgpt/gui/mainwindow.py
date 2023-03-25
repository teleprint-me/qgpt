from assistant.queue import MessageQueue
from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QStatusBar, QWidget

from .chat import ChatWidget
from .editor import EditorWidget
from .menubar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q-GPT")
        self.setGeometry(200, 200, 500, 500)

        # Set the message queue
        self.message_queue = MessageQueue()

        # Create menu bar
        menu_bar = MenuBar()
        self.setMenuBar(menu_bar)

        # Create ChatWidget and EditorWidget
        self.chat_widget = ChatWidget(self)
        self.editor_widget = EditorWidget()

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.chat_widget)
        main_layout.addWidget(self.editor_widget)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.update_status_bar()

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

    def closeEvent(self, event):
        # Save the queue state before exiting
        self.message_queue.save()
        # Exit program
        event.accept()
