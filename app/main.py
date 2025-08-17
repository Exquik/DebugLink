import sys      
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTabWidget, QMenuBar, QStatusBar
)
from PySide6.QtGui import QAction 

from ui.console_tab import ConsoleTab
from ui.plot_tab import PlotTab
from ui.settings_tab import SettingsTab



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("DebugLing - MVP") 
        self.resize(800, 600)

    #-------------Меню---------------
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        view_menu = menu_bar.addMenu("View")
        help_menu = menu_bar.addMenu("Help")

        exit_action =  QAction ("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)


        self.setMenuBar(menu_bar)

        tabs=QTabWidget()
        tabs.addTab(ConsoleTab(), "Console")
        tabs.addTab(PlotTab(), "Plot")
        tabs.addTab(SettingsTab(), "Settings")

        self.setCentralWidget(tabs)

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Добро пожаловать в DebugLink!")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()