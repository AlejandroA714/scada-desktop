from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, QThreadPool
from ..utils.session import session

class widgetSignals(QObject):

    sucess = pyqtSignal(object)

class widget(QWidget):

    threadpool = QThreadPool()

    def __init__(self,Parent=None):
        self.signals = widgetSignals()
        QWidget.__init__(self,Parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.session = session() # Automatic get session from program

    def sucess(self, result:object,text):
        reply = QMessageBox.question(
            self, "Confirmacion",
            text,
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.sucess.emit(result)
            self.close()
        else:
            pass


