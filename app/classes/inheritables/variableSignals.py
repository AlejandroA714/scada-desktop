from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

class variableSignals(object):
    updating = pyqtSignal()
    status_changed = pyqtSignal()