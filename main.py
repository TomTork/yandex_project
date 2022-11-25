import sys

import PyQt5
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.par = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.par:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow))
            painter.drawEllipse(random.randint(0, 600), random.randint(0, 600), random.randint(0, 600),
                                random.randint(0, 600))
            painter.end()
            self.par = False

    def run(self):
        self.par = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())