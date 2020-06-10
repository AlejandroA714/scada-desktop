from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from ..objects import device

class deviceSignals(QObject):
    updating = pyqtSignal()
    updated = pyqtSignal()
    report_emitted = pyqtSignal()
    status_changes = pyqtSignal()
    error = pyqtSignal(Exception)
    edit = pyqtSignal(device)
    copy = pyqtSignal(device)
    delete = pyqtSignal(device)


