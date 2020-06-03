from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, QThreadPool

class widgetSignals(QObject):

    sucess = pyqtSignal(object)

class widget(QWidget):

    threadpool = QThreadPool()

    def __init__(self,Parent=None):
        self.signals = widgetSignals()
        QWidget.__init__(self,Parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

    def sucess(self, result:object,text):
        reply = QMessageBox.question(
            self, "Confirmacion",
            text,
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.sucess.emit(result)
        else:
            pass


