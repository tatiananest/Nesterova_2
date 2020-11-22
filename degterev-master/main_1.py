import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setPen(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        for _ in range(random.randrange(2, 10)):
            x = random.randrange(10, 200)
            qp.drawEllipse(random.randrange(100, 300), random.randrange(200, 300), x,
                           x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
