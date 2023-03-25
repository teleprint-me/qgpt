from PySide6.QtWidgets import QLabel, QPlainTextEdit, QVBoxLayout, QWidget


class EditorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create developer column label
        self.text_label = QLabel("Editor:")

        # Create the text editor
        self.text_editor = QPlainTextEdit()

        # Create editor layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.text_editor)

        self.setLayout(self.layout)
