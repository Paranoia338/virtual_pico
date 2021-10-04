import random
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

class RectItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, rect=QtCore.QRectF()):
        super(RectItem, self).__init__(rect)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        self._pos_animation = QtCore.QVariantAnimation()
        self._pos_animation.valueChanged.connect(self.setPos)

    def move_smooth(self, end, duration=1000):
        if self._pos_animation.state() == QtCore.QAbstractAnimation.Running:
            self._pos_animation.stop()
        self._pos_animation.setDuration(duration)
        self._pos_animation.setStartValue(self.pos())
        self._pos_animation.setEndValue(end)
        self._pos_animation.start()

    def itemChange(self, change, value):
        if change ==QtWidgets.QGraphicsItem.ItemPositionChange:
            color = QtGui.QColor(QtCore.Qt.red)
            if self.scene().collidingItems(self):
                color = QtGui.QColor(QtCore.Qt.green)
            self.setPen(QtGui.QPen(color, 3))
        return super(RectItem, self).itemChange(change, value)

def move_pos(scene):
    for it in scene.items():
        pos = QtCore.QPointF(*random.sample(range(-100, 200), 2))
        if hasattr(it, 'move_smooth'):
            it.move_smooth(pos, 1000)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    scene = QtWidgets.QGraphicsScene(-100, -100, 200, 200)
    scene.setBackgroundBrush(QtCore.Qt.gray)
    view = QtWidgets.QGraphicsView(scene)
    view.resize(640, 480)
    view.show()
    l = []
    for _ in range(4):
        pos = QtCore.QPointF(*random.sample(range(-100, 200), 2))
        it = RectItem(QtCore.QRectF(-20, -20, 40, 40))
        scene.addItem(it)
        it.setPos(pos)
        l.append(it)
    wrapper = partial(move_pos, scene)
    timer = QtCore.QTimer(interval=3000, timeout=wrapper)
    timer.start()
    wrapper()
    sys.exit(app.exec_())