import sys

from PyQt5.QtCore import QPointF, QRectF, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QGraphicsObject, QApplication, QGraphicsView, \
    QGraphicsScene


class Resizer(QGraphicsObject):

    resizeSignal = pyqtSignal(QGraphicsItem.GraphicsItemChange, QPointF)

    def __init__(self, rect=QRectF(0, 0, 10,  10), parent=None):
        super().__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)

        # self.setCursor(Qt.SizeFDiagCursor)

        self.setCursor(Qt.SizeHorCursor)

        self.rect = rect
        self.hide()

    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            pen = QPen()
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.setRenderHint(QPainter.Antialiasing)
        painter.drawEllipse(self.rect)
        self.update()

    def itemChange(self, change, value):
        self.prepareGeometryChange()
        if change == QGraphicsItem.ItemPositionChange:
            if self.isSelected():
                self.resizeSignal.emit(change, self.pos())
        return super(Resizer, self).itemChange(change, value)

'''END CLASS'''

class GraphicLayer(QGraphicsPixmapItem):

    def __init__(self, top_left_x, top_left_y, graphic, rect=QRectF(0, 0, 100, 100), parent=None, scene=None):
        super().__init__(parent=parent)
        self.rect = rect
        self.setPixmap(graphic)
        self.graphic = graphic
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.setPos(top_left_x, top_left_y)

        # Resizer actions
        self.resizer_right = Resizer(parent=self)
        self.resizer_left = Resizer(parent=self)

        r_width = self.resizer_right.boundingRect().width() - 2
        self.r_offset = QPointF(r_width, r_width)

        l_width = self.resizer_left.boundingRect().left() + 2
        self.l_offset = QPointF(r_width, r_width)

        self.resizer_right.setPos(QPointF(self.boundingRect().right() + 10, self.boundingRect().y() + self.boundingRect().height()/2))
        self.resizer_right.resizeSignal.connect(self.resize)

        self.resizer_left.setPos(QPointF(self.boundingRect().left() - 10, self.boundingRect().y() + self.boundingRect().height()/2))
        self.resizer_left.resizeSignal.connect(self.resize)

    def set_tag(self, item_id):
        self.tag = item_id

    def get_tag(self):
        return self.tag

    def hoverMoveEvent(self, event):
        if self.isSelected():
            self.resizer_right.show()
            self.resizer_left.show()
        else:
            self.resizer_right.hide()
            self.resizer_left.hide()

    def hoverLeave(self, event):
        self.resizer_right.hide()
        self.resizer_left.hide()

    # @pyqtSlot()
    def resize(self, change, value):
        pixmap = self.graphic.scaled(value.x(), value.y()*2, transformMode=Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.prepareGeometryChange()
        self.update()

"""END OF CLASS"""


def main():

    app = QApplication(sys.argv)

    grview = QGraphicsView()
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, 680, 459)

    # scene.addPixmap(QPixmap('01.png'))
    pixds = QPixmap('avatar-icon.png')
    grview.setScene(scene)

    # item = GraphicsRectItem(0, 0, 300, 30)

    item = GraphicLayer(0, 0, pixds, scene=scene)
    scene.addItem(item)

    # grview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
    grview.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()