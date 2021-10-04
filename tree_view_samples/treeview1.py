import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class StandardItemModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(StandardItemModel, self).__init__(parent)

    def itemList(self, parent=QtCore.QModelIndex()):
        items = []
        for row in range(self.rowCount(parent)):
            idx = self.index(row, 0, parent)
            # items.append(self.data(idx))
            if self.hasChildren(idx):
                items.append(self.itemList(idx))
        return items

    def populate(self):
        for row in range(0, 10):
            parentItem = self.invisibleRootItem()
            for col in range(0, 4):
                item = QtGui.QStandardItem("item (%s, %s)" % (row, col))
                parentItem.appendRow(item)
                parentItem = item


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.model = StandardItemModel()
        self.model.populate()

        self.view = QtWidgets.QTreeView()
        self.view.setModel(self.model)
        self.view.setHeaderHidden(True)
        self.view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.setCentralWidget(self.view)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()
    for x in form.model.itemList():
        print(x)

if __name__ == '__main__':
    main()


































# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
# from PyQt5.QtCore import  Qt
# from PyQt5.QtGui import QFont, QColor, QImage, QStandardItemModel, QStandardItem
#
# class StandardItem(QStandardItem):
#     def __init__(self, txt='', image_path='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
#         super().__init__()
#
#         fnt = QFont('Open Sans', font_size)
#         fnt.setBold(set_bold)
#
#         self.setEditable(False)
#         self.setForeground(color)
#         self.setFont(fnt)
#         self.setText(txt)
#
#         if image_path:
#             image = QImage(image_path)
#             self.setData(image, Qt.DecorationRole)
#
# class AppDemo(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.resize(1200, 1200)
#
#         treeView = QTreeView()
#         treeView.setHeaderHidden(True)
#         treeView.header().setStretchLastSection(True)
#
#         treeModel = QStandardItemModel()
#         rootNode = treeModel.invisibleRootItem()
#
#         photos = StandardItem('My Photos', '', set_bold=True)
#
#         cat = StandardItem('Cats', './Images/cat.jpg', 14)
#         photos.appendRow(cat)
#
#         taipei = StandardItem('Taipei', './Images/taipei.jpg', 16)
#         photos.appendRow(taipei)
#
#         rootNode.appendRow(photos)
#         treeView.setModel(treeModel)
#         treeView.expandAll()
#
#         self.setCentralWidget(treeView)
#
# app = QApplication(sys.argv)
# demo = AppDemo()
# demo.show()
# sys.exit(app.exec_())