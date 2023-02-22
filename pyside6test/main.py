import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

from mainwindow import MainWindow

app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec())
