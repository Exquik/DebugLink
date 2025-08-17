from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PlotTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Здесь будет график данных"))
        self.setLayout(layout)