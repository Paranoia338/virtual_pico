import sys

from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen, QPixmap, QCursor
from PyQt5.QtWidgets import QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QMenu, \
    QAction, QInputDialog, QGraphicsTextItem


class GraphicsRectItem(QGraphicsRectItem):

    handleMiddleLeft = 4
    handleMiddleRight = 5

    handleSize = +15.0
    # handleSpace = -4.0
    handleSpace = +2.0

    handleCursors = {
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
    }

    def __init__(self, *args, stimuli_color=None):
        """
        Initialize the shape.
        """
        self.color = stimuli_color

        super().__init__(*args)

        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.updateHandlesPos()

        self.tag = None
        self.duration_width = None
        self.duration_text = None

        self.mouseMoveEventPos = None

        self.old_boundingRect = None
        self.difference_in_width = None


    def setTag(self, text):
        self.tag = text
        self.update()

    def getTag(self):
        return self.tag

    def setColor(self, color):
        self.color = color
        # self.update()

    def set_duration(self, duration_in_pixels=240, duration_in_milliseconds="Not available "):
        self.duration_width = duration_in_pixels
        self.duration_text = duration_in_milliseconds
        # self.update()

    # def get_current_width(self):
    #     # print(self.rect().width())
    #     return self.rect().width()


    def handleAt(self, point):
        """
        Returns the resize handle below the given point.
        """
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        """
        Executed when the mouse moves over the shape (NOT PRESSED).
        """
        if self.isSelected():
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        """
        Executed when the mouse leaves the shape (NOT PRESSED).
        """
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(moveEvent)

    def mousePressEvent(self, mouseEvent):
        """
        Executed when the mouse is pressed on the item.
        """
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        """
        Executed when the mouse is being moved over the item while being pressed.
        """
        self.mouseMoveEventPos = mouseEvent.pos()

        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        """
        Executed when the mouse is released from the item.
        """
        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()

    def boundingRect(self):
        """
        Returns the bounding rect of the shape (including the resize handles).
        """
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self, old_boundingRect=None, difference_in_width=None):
        """
        Update current resize handles according to the shape size and position.
        """
        s = self.handleSize
        b = self.boundingRect()
        self.handles[self.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        # self.handles[self.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        if old_boundingRect is not None:
            self.handles[self.handleMiddleRight] = QRectF(old_boundingRect.right() + difference_in_width - s, old_boundingRect.center().y() - s / 2, s, s)
        else:
            self.handles[self.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)

    def interactiveResize(self, mousePos):
        """
        Perform shape interactive resize.
        """
        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleMiddleLeft:
            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleRight:
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)
            self.setRect(rect)
        self.updateHandlesPos()

    def shape(self):
        """
        Returns the shape of this item as a QPainterPath in local coordinates.
        """
        path = QPainterPath()
        path.addRect(self.rect())
        if self.isSelected():
            for shape in self.handles.values():
                path.addEllipse(shape)
        return path

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        painter.setRenderHint(QPainter.Antialiasing)

        # rect_border_pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        rect_brush = QBrush(self.color)

        # handle_border_pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        handle_brush = QBrush(Qt.darkGreen)

        when_item_selected_pen = QPen(Qt.red, 2, Qt.DashDotLine, Qt.RoundCap, Qt.RoundJoin)

        if self.isSelected():
            for handle, rect in self.handles.items():
                painter.setBrush(handle_brush)
                painter.setPen(QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
                painter.drawEllipse(rect)
            painter.setBrush(rect_brush)
            painter.setPen(when_item_selected_pen)
            painter.drawRect(self.rect())

        # for handle, rect in self.handles.items():
        #     if self.handleSelected is None or handle == self.handleSelected:
        #         painter.setBrush(handle_brush)
        #         painter.setPen(Qt.NoPen)
        #         painter.drawEllipse(rect)
        painter.setBrush(rect_brush)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        if self.tag is not None:
            painter.setPen(QPen(QColor(Qt.black), 1.0, Qt.SolidLine))
            font = painter.font()
            font.setPointSize(font.pointSize() * 2)
            painter.setFont(font)
            painter.drawText(self.rect(), Qt.AlignVCenter | Qt.AlignLeft, self.tag)
            # self.tag = None

        if self.duration_text is not None:
            painter.setPen(QPen(QColor(Qt.black), 1.0, Qt.SolidLine))
            font = painter.font()
            font.setPointSize(font.pointSize() // 2)
            painter.setFont(font)
            painter.setBrush(QColor(Qt.black))
            painter.drawText(self.rect(), Qt.AlignVCenter | Qt.AlignRight, self.duration_text)
            # self.duration_text = None

        if self.duration_width is not None:
            pass
            # self.prepareGeometryChange()
            # self.boundingRect().setWidth(self.duration_width)
            # self.rect().setWidth(self.duration_width)




# def main():
#
#     app = QApplication(sys.argv)
#
#     grview = QGraphicsView()
#     scene = QGraphicsScene()
#     scene.setSceneRect(0, 0, 680, 459)
#
#     # scene.addPixmap(QPixmap('01.png'))
#     grview.setScene(scene)
#
#     item2 = GraphicsRectItem(0, 0, 300, 150, stimuli_color=QColor("#9000FF"))
#     scene.addItem(item2)
#
#     grview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
#     grview.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()