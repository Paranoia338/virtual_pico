import math

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from main_files.different_windows import StimuliParameters, TagWindow, DurationWindow
from widgets.timeline_pad_item import TimelinePad
from widgets.rect_shape_item import GraphicsRectItem
from widgets.line_shape_item import GraphicLayer


class MyGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.list_of_items = []
        self.context_position = None
        self.context_in_scene = None
        self.last_selected = None

        self.stimuli_color = QColor(0, 0, 255, 180)
        self.pixmap_item = QPixmap(r'C:\Users\Andrei Vantur\PycharmProjects\PicoScope\resources\handle.png')
        self.stimuli_image = 0
        self.stimuli_parameters_window = StimuliParameters()
        self.tag_naming_window = TagWindow()
        self.stimuli_duration_window = DurationWindow()

        # settings
        self.grid_size = 20
        self.grid_sqr = 2
        self.product = self.grid_size * self.grid_sqr

        # self._color_background = QColor("#393939")
        self._color_background = QColor("#343D46")

        """ Creating the light and dark pens """
        self._color_light = QColor("#2f2f2f")  # Used for the background grid
        self._color_dark = QColor("#292929")  # Used for the ticker color of the lanes
        self._pen_light = QPen(self._color_light)
        self._pen_dark = QPen(self._color_dark)
        self._pen_light.setWidth(1)
        self._pen_dark.setWidth(2)
        """ Additionally we can use a light or green pen for writing the thicker lines of the lanes """
        self._color_green = QColor("#96FF96")  # "#96FF96"  "#499C54"
        self._pen_green = QPen(self._color_green)
        self._pen_green.setWidth(1)

        self.scene_width = 2400
        self.scene_height = 1800

        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)
        # self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width//2, self.scene_height//2)

        self.setBackgroundBrush(self._color_background)

        self.pad_item = TimelinePad(pad_height=self.scene_height, start_x=(-self.scene_width // 2)+5, start_y=(-self.scene_height // 2)+5, scene=self)
        self.addItem(self.pad_item)



        """ Here we are going to define the context menu """
        self.sceneContextMenu = QMenu()
        """ Here we create the options inside the quick menu and the functions which will be triggered by them"""
        self.create_stimuli = QAction("1. Create stimuli")
        self.create_stimuli.triggered.connect(self.createStimuli)

        self.change_color_stimuli = QAction("2. Change color")
        self.change_color_stimuli.triggered.connect(self.changeStimuliColor)

        self.re_shape = QAction("3. Change stimuli shape to line")
        self.re_shape.setCheckable(True)
        self.re_shape.triggered.connect(self.changeStimuliAspect)

        # self.delete_stimuli = QAction("4. Delete stimuli")
        # self.delete_stimuli.triggered.connect(self.deleteStimuli)

        self.clean_scene = QAction("4. Clear scene")
        self.clean_scene.triggered.connect(self.clearScene)

        """ Here we add all the actions under the form of an iterable inside our context menu item """
        # self.sceneContextMenu.addActions(
        #     [self.create_stimuli, self.change_color_stimuli, self.re_shape, self.delete_stimuli, self.clean_scene])
        self.sceneContextMenu.addActions(
            [self.create_stimuli, self.change_color_stimuli, self.re_shape, self.clean_scene])

        # _______________________________________________________________

        self.itemMenu = QMenu()

        self.params_window = QAction("Parameters")
        self.params_window.triggered.connect(self.open_stimuli_params_window)

        self.duration = QAction("Set duration")
        # self.duration.triggered.connect(self.set_duration)
        self.duration.triggered.connect(self.open_duration_dialog)

        self.putTag = QAction("Add tag")
        self.putTag.triggered.connect(self.open_input_dialog)

        self.delTag = QAction("Delete tag")
        self.delTag.triggered.connect(self.deleteTag)

        self.changeColor = QAction("Update color")
        self.changeColor.triggered.connect(self.updateItemColor)

        self.delete_itm = QAction("Delete stimuli")
        self.delete_itm.triggered.connect(self.delete_item)

        # self.itemMenu.addActions(
        #     [self.params_window, self.duration, self.putTag, self.delTag, self.changeColor, self.delete_itm])
        self.itemMenu.addActions(
            [self.params_window, self.putTag, self.delTag, self.changeColor, self.delete_itm])
        # self.itemMenu.addActions([self.params_window, self.putTag, self.delTag, self.changeColor])

    """ The method for drawing multiple lines on out scene """

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        """ Here we will create our grid """
        _left = int(math.floor(rect.left()))
        _right = int(math.ceil(rect.right()))
        _top = int(math.floor(rect.top()))
        _bottom = int(math.ceil(rect.bottom()))

        first_left = _left - (_left % self.grid_size)
        first_top = _top - (_top % self.grid_size)

        lines_light = []
        lines_dark = []

        """ Here we will compute all the lines that will be drawn """

        for x in range(first_left, _right, self.grid_size):
            if x % self.product != 0:
                lines_light.append(QLine(x, _top, x, _bottom))
                lines_light.append(QLine(x + 10, _top, x + 10, _bottom))
            else:
                # lines_dark.append(QLine(x, _top, x, _bottom))
                lines_light.append(QLine(x, _top, x, _bottom))
                lines_light.append(QLine(x + 10, _top, x + 10, _bottom))

        for y in range(first_top, _bottom, self.grid_size):
            if y % self.product != 0:
                lines_light.append(QLine(_left, y, _right, y))
                lines_light.append(QLine(_left, y + 10, _right, y + 10))
                lines_light.append(QLine(_left, y + 20, _right, y + 20))
                lines_light.append(QLine(_left, y + 30, _right, y + 30))
            else:
                lines_dark.append(QLine(_left, y - 20, _right, y - 20))

        """ Here we draw the computed lines """
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        painter.setPen(self._pen_green)
        painter.drawLines(*lines_dark)

    """ The context menu event for opening right click options """

    def contextMenuEvent(self, event):
        """ The position of the mouse relative to the entire screen """
        self.context_position = QCursor.pos()
        """ The position of the mouse relative to the scene """
        self.context_in_scene = event.scenePos()

        self.scene_mouse_position_x = event.scenePos().x()
        # print(self.scene_mouse_position_x)
        self.scene_mouse_position_y = event.scenePos().y()
        # print(self.scene_mouse_position_y)
        # self.sceneContextMenu.exec_(self.context_position)
        items_at = self.items(event.scenePos())
        if len(items_at) == 0:
            self.sceneContextMenu.exec_(self.context_position)
        else:
            self.itemMenu.exec_(self.context_position)

    """ These functions run from the context menu self.itemMenu """

    def open_stimuli_params_window(self):
        self.stimuli_parameters_window.show()

    # def set_duration(self):
    #     pass

    def open_duration_dialog(self):
        self.stimuli_duration_window.signal_duration.stimuli_duration_signal.connect(self.process_stimuli_duration)
        self.stimuli_duration_window.show()

    def process_stimuli_duration(self, time_value):
        time = time_value.toPyTime()
        print(time)
        selected_items = self.selectedItems()
        self.last_selected = selected_items[0]
        # print(self.last_selected.get_id())
        # self.last_selected.set_duration()

    def open_input_dialog(self):
        self.tag_naming_window.signal_tag.tag_name.connect(self.addTag)
        self.tag_naming_window.show()

    def addTag(self, txt):
        selected_items = self.selectedItems()
        if len(selected_items) == 0:
            pass
        else:
            self.last_selected = selected_items[0]
            self.last_selected.setTag(txt)

    def deleteTag(self):
        selected_items = self.selectedItems()
        if len(selected_items) == 0:
            pass
        else:
            self.last_selected = selected_items[0]
            self.last_selected.setTag(None)

    def updateItemColor(self):
        selected_items = self.selectedItems()
        self.last_selected = selected_items[0]
        self.last_selected.setColor(self.stimuli_color)

    def delete_item(self):
        """ The approach for deleting items inside scene ( supports multiple deletion ) """
        selected_items = self.selectedItems()
        if len(selected_items) == 0:
            print("Nothing was selected")
            pass
        elif len(selected_items) == 1:
            self.last_selected = selected_items[0]
            print("It was selected: {}".format(self.last_selected))
            self.removeItem(self.last_selected)
            self.last_selected = None
        else:
            print("Many items had been selected")
            for i, item in enumerate(selected_items):
                print(f"Deleting the selected item from index: {i}")
                self.removeItem(item)

    # Here the methods for stimuli context menu stop __________________________________________________

    """ These functions run from the context menu self.sceneContextMenu """

    """ 1) This function creates the stimuli, currently under the shape of a rectangle """

    def createStimuli(self):
        if self.stimuli_image == 0:
            self.create_Rect_Stimuli(self.scene_mouse_position_x, self.scene_mouse_position_y, 120, 32,
                                     self.stimuli_color)

        elif self.stimuli_image == 1:
            self.create_Line_Stimuli(self.scene_mouse_position_x, self.scene_mouse_position_y)

    """ Here is the function which that the creation of a rectangle """

    def create_Rect_Stimuli(self, x_start, y_start, width, height, color):
        rect_item = GraphicsRectItem(x_start, y_start, width, height, stimuli_color=color)
        # self.list_of_items.append(rect_item)
        self.addItem(rect_item)

    """ Here is the function that triggers the creation of a QPixmap object (handle.png) """

    def create_Line_Stimuli(self, x_start, y_start):
        # rect_item = QRectF(x_start, y_start, 120, 32)
        rect_item = QRectF(0, 0, 120, 32)
        item = GraphicLayer(x_start, y_start, self.pixmap_item, rect_item, scene=self)
        self.addItem(item)

    """ 2) This function changes the look of the future stimuli"""

    def changeStimuliAspect(self):
        if self.re_shape.isChecked():
            self.re_shape.setText("3. Change stimuli shape to rectangle")
            self.stimuli_image = 1
        else:
            self.re_shape.setText("3. Change stimuli shape to Pixmap")
            self.stimuli_image = 0

    """ 3) This function changes the color of the future stimuli """

    def changeStimuliColor(self):
        color_function = QColorDialog.getColor()
        if color_function.isValid():
            hex_color = str(color_function.name())
            # print(hex_color)
            new_hex_color = hex_color.strip("#")
            # print(new_hex_color)
            self.convert_hex_to_rgb(new_hex_color, 100)

    def convert_hex_to_rgb(self, hex_str, transparency):
        hex_red = hex_str[0:-4]
        # print(hex_red)
        hex_green = hex_str[2:-2]
        # print(hex_green)
        hex_blue = hex_str[4:6]
        # print(hex_blue)
        self.stimuli_color = QColor(int(hex_red, 16), int(hex_green, 16), int(hex_blue, 16), transparency)

    # """ 4) This function deletes all the selected stimuli """
    #
    # def deleteStimuli(self):
    #     """ The approach for deleting items inside scene ( supports multiple deletion ) """
    #     selected_items = self.selectedItems()
    #     if len(selected_items) == 0:
    #         print("Nothing was selected")
    #         pass
    #     elif len(selected_items) == 1:
    #         self.last_selected = selected_items[0]
    #         print("It was selected: {}".format(self.last_selected))
    #         self.removeItem(self.last_selected)
    #         self.last_selected = None
    #     else:
    #         print("Many items had been selected")
    #         for i, item in enumerate(selected_items):
    #             print(f"Deleting the selected item from index: {i}")
    #             self.removeItem(item)

    """ 5) This function clears the entire scene of any item """

    def clearScene(self):
        self.clear()
        pad_item = TimelinePad(pad_height=self.scene_height, start_x=(-self.scene_width // 2)+5, start_y=(-self.scene_height // 2)+5, scene=self)
        self.pad_item = pad_item
        self.addItem(self.pad_item)


