
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QMessageBox,QPushButton

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.date_inster=QPushButton(text="数据录入")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())