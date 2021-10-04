from PyQt5.QtCore import QSize
from PyQt5.QtGui import QStandardItem, QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_zise=15, set_bold=False, color=QColor(0, 0, 0)):
        super(StandardItem, self).__init__()

        font = QFont('Open Sans', font_zise)
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(txt)
        """ Here we are setting the height of the rows from the treeview """
        self.setSizeHint(QSize(40, 40))
