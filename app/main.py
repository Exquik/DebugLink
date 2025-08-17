import sys      
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Заголовок окна
        self.setWindowTitle ("DebugLing - MVP")

        #размер окна
        self.resize(800, 600)

        label = QLabel("Добро пожаловать в DebugLink!, self")
        label.setStyleSheet("font-size: 18px; padding: 20px;")
        self.setCentralWidget(label)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()