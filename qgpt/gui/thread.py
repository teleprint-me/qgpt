from PySide6.QtCore import QThread, Signal


class ResponseThread(QThread):
    response_generated = Signal(str)

    def __init__(self, message_queue):
        super().__init__()
        self.message_queue = message_queue

    def run(self):
        response = self.message_queue.generate_completion()
        self.response_generated.emit(response)
