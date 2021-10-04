from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from test_folder.timeline_pad import TimelinePad


class AnnotationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AnnotationWindow, self).__init__(parent)
        self.m_view = QGraphicsView()
        self.m_scene = QGraphicsScene(self)
        self.m_scene.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        self.scene_width = 640
        self.scene_height = 480

        self.m_scene.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)

        self.m_view.setScene(self.m_scene)
        self.setCentralWidget(self.m_view)

        x = TimelinePad(pad_height=1000, start_x=2, start_y=2)
        self.m_scene.addItem(x)
        self.m_view.setAlignment(Qt.AlignTop | Qt.AlignLeft)



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = AnnotationWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())