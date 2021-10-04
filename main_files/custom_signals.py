from PyQt5.QtCore import QObject, pyqtSignal, QTime


class TreeViewCustomSignal(QObject):
    tip_signal_gr = pyqtSignal(str)
    tip_signal_sim = pyqtSignal(str)


class Signals(QObject):
    tag_name = pyqtSignal(str)
    stimuli_duration_signal = pyqtSignal(QTime)


class ZoomSignals(QObject):
    zoom_in = pyqtSignal(int)
    zoom_out = pyqtSignal(int)
