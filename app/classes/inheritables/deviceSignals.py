from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

class deviceSignals(QObject):
    updating = pyqtSignal()
    updated = pyqtSignal()
    report_emitted = pyqtSignal()
    status_changes = pyqtSignal()
    error = pyqtSignal(Exception)


