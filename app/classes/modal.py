from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt,QObject, pyqtSlot, pyqtSignal


class modalSignals(QObject): # A class to emit signals at execution

    canceled = pyqtSignal()
    success = pyqtSignal(object)

class modal(QDialog): # Class to be inherit to convert a window into a modal
    
    signals = modalSignals() # Instance signals to be emited

    def __init__(self,Parent): #Parent must be a QMainWindow
        QDialog.__init__(self,Parent)
        self.setWindowFlags(Qt.FramelessWindowHint) # removes borders
        self.setAttribute(Qt.WA_TranslucentBackground) # Making it translucent to make a trick with the shadows
        self.center(Parent)

    def center(self,parent:QMainWindow): # this function is responsible for centering the modal with respect its father
        qr = self.frameGeometry()
        qr.moveTo(parent.rect().center())

    def exit(self): # this function is responsible to emit a cancelation signal if exit button was clicked
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea cancelar?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.canceled.emit()
            self.close()
        else:
            pass
    
    def success(self,_x:object): # this function is responsible to emit a success signal, if dialog was success
        self.signals.success.emit(_x)
        self.close()
