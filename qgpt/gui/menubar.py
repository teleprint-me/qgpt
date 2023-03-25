from assistant import MessageQueue
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QFileDialog, QMenuBar, QMessageBox


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create File menu and add Exit action
        file_menu = self.addMenu("File")

        # Create Open, Save, and Exit actions
        openFile = QAction("Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.open_file)

        saveFile = QAction("Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.triggered.connect(self.save_file)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.exit_app)

        # Add actions to File menu
        file_menu.addAction(openFile)
        file_menu.addAction(saveFile)
        file_menu.addAction(exitAction)

        #
        # Create chat menu
        #
        message_queue = MessageQueue()
        chat_menu = self.addMenu("Chat")

        # Create chat save action
        save_action = QAction("Save", self)
        save_action.triggered.connect(message_queue.save)

        # Create chat load action
        load_action = QAction("Load", self)
        load_action.triggered.connect(message_queue.load)

        # Create chat clear action
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(message_queue.clear)

        # Add chat actions
        chat_menu.addAction(save_action)
        chat_menu.addAction(load_action)
        chat_menu.addAction(clear_action)

        # Create Help menu and add About action
        help_menu = self.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    def open_file(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)"
        )
        if fileName:
            with open(fileName, "r") as file:
                self.textEditor.setPlainText(file.read())

    def save_file(self):
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)"
        )
        if fileName:
            with open(fileName, "w") as file:
                file.write(self.textEditor.toPlainText())

    @Slot()
    def show_about_dialog(self):
        QMessageBox.about(
            self,
            "About Q-GPT",
            "Q-GPT is a QT GUI Toolkit that integrates GPT models as first-class components in the application. It provides an easy way to create GUI applications that interact with GPT models, enabling seamless communication and response handling.",
        )

    @Slot()
    def exit_app(self):
        QApplication.quit()
