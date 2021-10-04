from PyQt5.QtCore import QPoint, Qt, pyqtSignal, pyqtProperty, QObject, QVariantAnimation, QAbstractAnimation, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygon, QPolygonF, QColor
from PyQt5.QtWidgets import QGraphicsPolygonItem, QGraphicsItem


class TimelinePad(QGraphicsPolygonItem):
    def __init__(self, pad_height=500, start_x=10, start_y=10, scene=None):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.scene_h = pad_height

        self.scene = scene
        self.position_animation = QVariantAnimation()
        self.position_animation.valueChanged.connect(self.setPos)

        # _darkMagenta_brush = QBrush(Qt.darkMagenta)
        # _black_pen = QPen(Qt.black)
        #
        # self.setPen(_black_pen)
        # self.setBrush(_darkMagenta_brush)

        self.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        self.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        polygon_points = [QPoint(self.start_x, self.start_y), QPoint(self.start_x, self.start_y + 20), QPoint(self.start_x + 3, self.start_y + 25), QPoint(self.start_x + 3, self.scene_h), QPoint(self.start_x + 7, self.scene_h), QPoint(self.start_x + 7, self.start_y + 25), QPoint(self.start_x + 10, self.start_y + 20), QPoint(self.start_x + 10, self.start_y)]

        pad = QPolygonF(polygon_points)
        self.setPolygon(pad)
        # self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)


    def move(self, duration=1000, pixels=1000):
        self.position_animation.setDuration(duration)
        self.position_animation.setStartValue(self.pos())
        self.position_animation.setEndValue(QPointF(self.pos().x() + pixels, self.pos().y()))
        self.position_animation.start()

