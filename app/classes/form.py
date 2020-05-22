import PyQt5
from PyQt5.QtCore import Qt,QObject, pyqtSlot, pyqtSignal, QThreadPool
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
from resources.resources import *

class formSignals(QObject):

    login = pyqtSignal(object)
    logout = pyqtSignal()
    finish = pyqtSignal()
    error = pyqtSignal(Exception)

class form(QMainWindow): # class to be inherit to make a main window

    threadpool = QThreadPool()
    signals = formSignals()
    session = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.center()
        self.setWindowIcon(QIcon(':/source/img/if_16_1751363.ico'))
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def exit(self,event):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea salir?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.finish.emit()
            if not (isinstance(event,bool)) : event.accept()
        else:
            if not (isinstance(event,bool)) : event.ignore()
