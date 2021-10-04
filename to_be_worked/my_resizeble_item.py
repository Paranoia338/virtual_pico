import typing

from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QPen, QTextOption, QPainter
from PyQt5.QtWidgets import QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsItem, QWidget, \
    QStyleOptionGraphicsItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QPointF, QRectF

""" This class is responsible for creating the custom item which is the Stimuli """


class MyCustomText(QGraphicsTextItem):
    def __init__(self, tag_text):
        super().__init__()

        self.tag = tag_text

    def boundingRect(self):
        return QRectF


class Stimuli(QGraphicsItem):
    def __init__(self, x, y, w, h, color):
        super().__init__()

        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.painter = QPainter()
        self.text = "Hi there!"

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

        self.rectangle = None

    def boundingRect(self):
        return QRectF(self.x, self.y, self.w, self.h)

    # : QtGui.QPainter
    # item.setFlag(QGraphicsItem.ItemIsMovable)

    def paint(self, painter=None, option=None, widget=None):
        brush = QBrush(self.color)
        self.rectangle = self.boundingRect()

        self.tag = QGraphicsTextItem()

        painter.fillRect(self.rectangle, brush)
        painter.drawText(self.rectangle, self.text)
        painter.drawRect(self.rectangle)


    def re_tag(self, text="Salut!"):
        self.text = text
        self.paint()



    def paintEvent(self):
        self.painter.drawText(self, self.text)
