import sys

from PySide6.QtCore import QObject, Signal, Slot, QMetaObject
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI
        # -------------自定义功能函数---------------------

        # -------------事件和槽连接处理函数---------------------
        self.ui.pushButton_2.clicked.connect(self.btnclick)

    # -------------自动关联槽函数---------------------
    @Slot()
    def on_pushButton_clicked(self):
        self.ui.label.setText('测试')

    # -------------自定义的槽函数---------------------
    def btnclick(self):
        self.ui.label_2.setText('测试')


# -------------窗体测试程序---------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
