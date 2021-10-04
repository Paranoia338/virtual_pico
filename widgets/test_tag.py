import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from widgets.tag_window import Ui_Tag


class TagWindow:
    def __init__(self):
        self.main_window = QMainWindow()
        self.gui = Ui_Tag()
        self.gui.setupUi(
            self.main_window)

    def show(self):
        self.main_window.show()


if __name__ == "__main__":
    app_context = QApplication(sys.argv)
    mainWindow = TagWindow()
    mainWindow.show()
    sys.exit(app_context.exec_())