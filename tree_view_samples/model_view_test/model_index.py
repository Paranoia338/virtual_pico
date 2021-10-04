import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import json

# class StandardItemModel(QtGui.QStandardItemModel):
#     def __init__(self, parent=None):
#         super(StandardItemModel, self).__init__(parent)
#
#         items = ["Gabriela", "Ionut", "Andrei", "Irinel", "Vasile", "Ion", "Gheorghe"]
#
#       def populate(self):
#           for x in range(0, len(self.items)):

#
# def itemList(self, parent=QtCore.QModelIndex()):
#     items = []
#     for row in range(self.rowCount(parent)):
#         idx = self.index(row, 0, parent)
#         items.append(self.data(idx))
#         if self.hasChildren(idx):
#             items.append(self.itemList(idx))
#     return items
#
# def populate(self):
#     for row in range(0, 10):
#         parentItem = self.invisibleRootItem()
#         for col in range(0, 4):
#             item = QtGui.QStandardItem("item (%s, %s)" % (row, col))
#             parentItem.appendRow(item)
#             parentItem = item
from PyQt5.QtCore import QModelIndex, QVariant
from PyQt5.QtGui import QStandardItemModel, QColor, QCursor
from PyQt5.QtWidgets import QMenu, QAction, QTreeWidgetItem, QAbstractItemView
from main_files.different_windows import AddItemsToList
from PyQt5.QtGui import QStandardItem, QFont, QColor


class MyItem(QStandardItem):
    def __init__(self, txt='', set_bold=False, color=QColor(0, 0, 0)):
        super(MyItem, self).__init__()

        font = QFont('Open Sans')
        font.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(font)
        self.setText(txt)
        """ Here we are setting the height of the rows from the treeview """
        # self.setSizeHint(QSize(40, 40))


the_list = ["Gabriela", "Ionut", "Andrei", "Irinel", "Vasile", "Ion", "Gheorghe"]


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None, item_list=None):
        super(MainForm, self).__init__(parent)
        if item_list is None:
            # item_list = ["Andrei", "Vantur"]
            item_list = [{"Andrei": ["Mata", "Tactu"]}, {"Vantur": ["Sorta", "Fractu"]}]
        self.name_group_window = AddItemsToList('group')
        self.name_simu_window = AddItemsToList('simulation')

        self.name_group_window.signal_tree_view.tip_signal_gr.connect(self.create_new_group)
        self.name_simu_window.signal_tree_view.tip_signal_sim.connect(self.create_new_simulation)

        self.list_menu = QMenu()
        self.create_group = QAction("Add group")
        self.create_stimuli = QAction("Add simulation")
        self.get_list = QAction("Get list")
        self.delete_element = QAction("Delete element")

        self.create_group.triggered.connect(self.addGroupToList)
        self.create_stimuli.triggered.connect(self.addSimulation)
        self.get_list.triggered.connect(self.print_list)
        self.delete_element.triggered.connect(self.remove_row)

        self.list_menu.addActions([self.create_group, self.create_stimuli, self.get_list, self.delete_element])

        self.contextMenuEvent = self.create_list_context_menu
        # -----------------------------------------------------------------------
        self.items = item_list

        # self.model = QStandardItemModel()
        # self.parentItem = self.model.invisibleRootItem()
        # self.model = QTreeWidgetItem()

        # self.new_items = []
        keys = []
        values = []

        lista_iteme = []

        for x in self.items:
            key = list(x.keys())
            keys.append(key[0])
            value = list(x.values())
            values.append(value[0])

        print(keys)
        print(values)

        for y in range(0, len(keys)):
            item = QTreeWidgetItem(keys[y])
            self.parentItem.appendRow(QStandardItem(item))
            child_items = values[y]
            for z in child_items:
                child_item = QTreeWidgetItem(QStandardItem(z))
                item.addChild(child_item)
            lista_iteme.append(item)

        print(lista_iteme)
        # self.parentItem.appendRows(lista_iteme)

        # for x in range(0, len(self.keys)):
        #     item = QStandardItem(self.keys[x])
        #     self.new_items.append(item)
        #     # self.parentItem.appendRow(item)
        #
        # self.parentItem.appendRows(self.new_items)

        # self.view = QtWidgets.QTreeView()
        self.view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view = QtWidgets.QTreeWidget()
        # self.view.setModel(self.model)
        self.view.setHeaderHidden(True)
        self.view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.view.setIndentation(0)

        # for i in range(self.model.rowCount()):
        #     index = QModelIndex(self.model.index(i, 0))
        #     print(index)
        #     print(self.model.itemData(index)[0])

        self.setCentralWidget(self.view)

    def addGroupToList(self):
        self.name_group_window.gui.tag_text_edit.clear()
        self.name_group_window.gui.tag_text_edit.setFocus()
        self.name_group_window.show()

    def addSimulation(self):
        self.name_simu_window.gui.tag_text_edit.clear()
        self.name_simu_window.gui.tag_text_edit.setFocus()
        self.name_simu_window.show()

    def print_list(self):
        # for i in range(self.model.rowCount()):
        # print(self.view.)
        # print(self.view.currentIndex().column())
        # index = QModelIndex(self.model.index(i, 0))
        # print(index)
        # print(self.model.itemData(index)[0])
        print("-" * 300)

    def remove_row(self):
        selected_index = self.view.selectedIndexes()
        index = selected_index[0]
        # print(index)
        print(index.data())
        index_inside_items_list = self.items.index(index.data())
        # print(index_inside_items_list)
        print(self.items)
        self.items.pop(index_inside_items_list)
        print(self.items)
        self.model.removeRow(index.row())
        print("Randul: {} a fost sters".format(index.row()))

    def create_new_group(self, text):
        # print("Group", text)
        item = MyItem(text, color=QColor(0, 0, 0))
        self.items.append(text)
        self.parentItem.appendRow(item)

    def create_new_simulation(self, text):
        print("-" * 200)
        index_parent = QModelIndex(self.view.currentIndex())
        parent_row = index_parent.row()
        # parent_column = index_parent.column()
        # print(parent_row, parent_column)
        item = MyItem(text, color=QColor(0, 0, 0))
        self.reconstruct_tree(parent_row, item)
        # self.model.clear()

        # self.parentItem.setChild(0, 0, item)

        # parent_row = index.row()
        # parent_column = index.column()
        # print(parent_row, parent_column)
        # child_column = parent_column + 1
        # parent = QModelIndex(self.model.index(parent_row, parent_column))
        # self.model.insertRow(parent_row, parent)
        # self.model.insertColumn(parent_column, parent)
        # item = MyItem(text, color=QColor(0, 0, 0))
        # self.model.setData(self.model.index(parent_row, child_column, parent), item)
        # self.view.update()

        # print(self.model.parent())

        # self.model.beginInsertRows()

        # index = self.view.selectedIndexes()
        # dictionary = self.model.itemData(index[0])
        # print(dictionary.get(0))
        # secondParent = dictionary.get(0)

        # for a in range(0, self.parentItem.rowCount()):
        #     kid = self.parentItem.child(a)
        #     print(kid.data(0))

    def create_list_context_menu(self, event):
        self.list_menu.exec_(QCursor.pos())

    def reconstruct_tree(self, index, child):
        print(self.items[index])
        # for x in range(0, len(self.items)):
        #     item = QStandardItem(self.items[x])
        #     self.new_items.append(item)
        #     # self.parentItem.appendRow(item)
        #
        # self.parentItem.appendRows(self.new_items)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainForm(item_list=None)
    form.show()
    app.exec_()
    # print(form.model.itemList())


if __name__ == '__main__':
    main()
