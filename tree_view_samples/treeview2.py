import sys

from PyQt5 import QtWidgets, QtGui, QtCore


class StandardItemModel(QtGui.QStandardItemModel):
    def __init__(self, parent = None):
        super(StandardItemModel, self).__init__(parent)

    def itemList(self, parent = QtCore.QModelIndex()):
        items = []
        for row in range(self.rowCount(parent)):
            idx = self.index(row, 0, parent)
            items.append(self.data(idx))
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
    print(form.model.itemList())

if __name__ == '__main__':
    main()