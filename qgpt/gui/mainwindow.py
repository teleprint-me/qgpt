from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QStatusBar,
    QWidget,
)

from .chat import ChatWidget
from .editor import EditorWidget
from .menubar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self, message_queue):
        super().__init__()

        self.setWindowTitle("Q-GPT")
        self.setGeometry(200, 200, 500, 500)

        # Set the message queue
        self.message_queue = message_queue

        # Create menu bar
        menu_bar = MenuBar()
        self.setMenuBar(menu_bar)

        # Create ChatWidget and EditorWidget
        self.chat_widget = ChatWidget(self.message_queue, self.send_message)
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

    def send_message(self, message):
        # Process the message and update chat history and status bar
        # This method should be implemented based on your current Q_GPT.send_message() logic

        pass
