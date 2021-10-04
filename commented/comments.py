
# """ Sets the scene rectangle starting point and the dimensions """
# # self.grScene.setSceneRect(0, 0, 1000, 1000)
# """ Sets the scene inside the QGraphicsView viewport """
# self.gui.timeline.setScene(self.grScene)

# self.gui.list.setContextMenuPolicy(Qt.CustomContextMenu)
# self.gui.list.customContextMenuRequested.connect(self.create_list_context_menu)

# with h5py.File(file, "w") as hdf:
#     group_1 = hdf.create_group("Group 1")
#     group_1.create_dataset('dataset_1', data=commands_names)



# boundingRect = self.boundingRect()
# self.updateHandlesPos(boundingRect, difference_in_width)
#
# offset = self.handleSize + self.handleSpace
# rect = self.rect()
# self.prepareGeometryChange()
# boundingRect.setRight(boundingRect.right() + difference_in_width)
# rect.setRight(boundingRect.right() - offset)
# self.setRect(rect)



#ONLY FOR WIDGETS, FOR ITEMS YOU NEED QVariant Animation
# self.animation = QPropertyAnimation(self.pad_item, b"start_x", self)
# self.animation.setDuration(5000)
# self.animation.setStartValue(QPoint((-self.scene_width // 2)+5, (-self.scene_height // 2)+5))
# self.animation.setEndValue(QPoint((-self.scene_width // 2)+205, (-self.scene_height // 2)+5))
# self.animation.setEasingCurve(QEasingCurve.InOutCubic)



# def get_zero_pos(self):
#     self.initial_position = self.pos()

# def getValueX(self):
#     return self.start_x
#
# def setValueX(self, new_X):
#     self.start_x = new_X
#
# def getValueY(self):
#     return self.start_y
#
# def setValueY(self, new_Y):
#     self.start_y = new_Y

# value_X = pyqtProperty(float, getValueX, setValueX)
# value_Y = pyqtProperty(float, getValueY, setValueY)



# def move_smooth(self, end, duration=1000):
#     if self.position_animation.state() == QAbstractAnimation.Running:
#         self.position_animation.stop()
#     self.position_animation.setDuration(duration)
#     self.position_animation.setStartValue(self.pos())
#     self.position_animation.setEndValue(end)
#     self.position_animation.start()
#
# def itemChange(self, change, value):
#     if change == QGraphicsItem.ItemPositionChange:
#         color = QColor(Qt.red)
#         if self.scene().collidingItems(self):
#             color = QColor(Qt.green)
#         self.setPen(QPen(color, 3))
#     return super(TimelinePad, self).itemChange(change, value)


# the below line does not work here because we have a QTreeView and this works only with QTreeWidget
# selected_item = self.view.selectedItems()
# print(selected_item)