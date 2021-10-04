import sys

from PyQt5.QtCore import QPointF, QRectF, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QGraphicsObject, QApplication, QGraphicsView, \
    QGraphicsScene


class Resizer(QGraphicsObject):
    resizeSignal = pyqtSignal(QGraphicsItem.GraphicsItemChange, QPointF)

    def __init__(self, rect=QRectF(0, 0, 10, 10), parent=None, stimuli_color=Qt.red):
        super().__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setCursor(Qt.SizeFDiagCursor)
        self.rect = rect
        self.hide()

        self.color = stimuli_color

        self.tag = None

    def setTag(self, text):
        self.tag = text
        self.update()

    def getTag(self):
        return self.tag

    def setColor(self, color):
        self.color = color
        self.update()

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
    def __init__(self, top_left_x, top_left_y, graphic, rect=QRectF(0, 0, 100, 10), parent=None, scene=None):
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
        self.resizer = Resizer(parent=self)
        r_width = self.resizer.boundingRect().width() - 2
        self.r_offset = QPointF(r_width, r_width)
        self.resizer.setPos(self.boundingRect().bottomRight() - self.r_offset)
        self.resizer.resizeSignal.connect(self.resize)

    def set_tag(self, item_id):
        self.tag = item_id

    def get_tag(self):
        return self.tag

    def hoverMoveEvent(self, event):
        if self.isSelected():
            self.resizer.show()
        else:
            self.resizer.hide()

    def hoverLeave(self, event):
        self.resizer.hide()

    # @pyqtSlot()
    def resize(self, change, value):
        pixmap = self.graphic.scaled(value.x(), value.y(), transformMode=Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.prepareGeometryChange()
        self.update()


"""END OF CLASS"""

#
# def main():
#
#     app = QApplication(sys.argv)
#
#     grview = QGraphicsView()
#     scene = QGraphicsScene()
#     scene.setSceneRect(0, 0, 680, 459)
#     grview.setScene(scene)
#
#     pixds = QPixmap(r'C:\Users\Andrei Vantur\PycharmProjects\PicoScope\widgets\handle.png')
#
#     item = GraphicLayer(0, 0, pixds, scene=scene)
#     scene.addItem(item)
#
#     # grview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
#     grview.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
