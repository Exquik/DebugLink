from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ConsoleTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel ("Здесь будет консоль Rx/Tx"))
        self.setLayout(layout)