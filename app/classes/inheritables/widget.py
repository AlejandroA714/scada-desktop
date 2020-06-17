from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, QThreadPool
from ..utils.session import session

class widgetSignals(QObject):

    sucess = pyqtSignal(object)
    edit = pyqtSignal(object)
    delete = pyqtSignal(object)

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

    def prompt(self,title,text):
        reply = QMessageBox.question(
            self, title,
            text,
            QMessageBox.Yes | QMessageBox.No)
        return reply
