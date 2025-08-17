from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Здесь будут настройки"))
        self.setLayout(layout)