from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtWidgets import QGraphicsView

from main_files.custom_signals import ZoomSignals


class MyGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)

        self.zoom_signals = ZoomSignals()

        self.zoomClamp = False
        self.zoomInFactor = 1.25
        self.zoom = 1
        self.zoomStep = 1
        self.zoomRange = [0, 10]

        self.zoom_in_factor_buttons = 1.25
        self.zoom_counter = 0

        self.initUI()

        self.setScene(grScene)

    def initUI(self):
        """ Different options for the GraphicsView widget """
        # self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setInteractive(True)
        self.setMouseTracking(True)

        # self.centerOn(-1200, -900)
        """ Makes the scene borders visible """
        # self.setFrameShadow(QFrame.Raised)




    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        # print("MMB pressed")
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton,
                                   Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)

        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event):
        # print("MMB released")
        self.setDragMode(QGraphicsView.NoDrag)

        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() & Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(fakeEvent)

    def leftMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        """ Calculate our zoom factor """
        zoomOutFactor = 1 / self.zoomInFactor

        """ Calculate the zoom """
        if event.angleDelta().y() > 0:
            # print(event.angleDelta().y())
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            # print(event.angleDelta().y())
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        clamped = False
        if self.zoom < self.zoomRange[0]:
            self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1]:
            self.zoom, clamped = self.zoomRange[1], True

        """ Set scene scale """
        if not clamped or self.zoomClamp is True:  # If self.zoomClamp is False, we'll be able to zoom in more but this will make the app to crash if we zoom too much.
            self.scale(zoomFactor, zoomFactor)

    def zoom_from_buttons(self, event):
        """ Calculate the zoom """

        zoom_out_factor_buttons = 1 / self.zoom_in_factor_buttons

        if event == 0:
            self.scale(self.zoom_in_factor_buttons, self.zoom_in_factor_buttons)

        if event == 1:
            self.scale(zoom_out_factor_buttons, zoom_out_factor_buttons)

    def zoom_in(self):
        self.zoom_signals.zoom_in.connect(self.zoom_from_buttons)
        self.zoom_signals.zoom_in.emit(0)

    def zoom_out(self):
        self.zoom_signals.zoom_out.connect(self.zoom_from_buttons)
        self.zoom_signals.zoom_out.emit(1)
