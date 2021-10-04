from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygon
from PyQt5.QtWidgets import QGraphicsRectItem


class AnimationItem(QGraphicsRectItem):
    # _transparent_pen = QPen(Qt.transparent)
    _darkMagenta_brush = QBrush(Qt.darkMagenta)
    _black_pen = QPen(Qt.black)

    def __init__(self, parent=None, duration=None, start_x=None, start_y=None, end_x=None, end_y=None, scene_height=None):
        super().__init__(parent)
        self.duration = duration
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.scene_h = scene_height


    def paintEvent(self, painter):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(self._black_pen)
        painter.setBrush(self._darkMagenta_brush)

        poligon = QPolygon([QPoint(self.start_x, self.start_y), QPoint(self.start_x, self.start_y + 20), QPoint(self.start_x + 4, self.start_y + 25), QPoint(self.start_x + 4, self.scene_h), QPoint(self.start_x + 6, self.start_y + 25), QPoint(self.start_x + 10, self.start_y + 20), QPoint(self.start_x + 10, self.start_y)])
