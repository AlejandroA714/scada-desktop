from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt,QObject, pyqtSlot, pyqtSignal, QThreadPool


class modalSignals(QObject): # A class to emit signals at execution

    canceled = pyqtSignal()
    success = pyqtSignal(object)

class modal(QDialog): # Class to be inherit to convert a window into a modal
    
    def __init__(self,Parent,session = None): #Parent must be a QMainWindow
        self.signals = modalSignals() # Instance signals to be emited
        self.threadpool = QThreadPool() #QThearPool object to execute work class
        self.__session = None # session object
        self.__parent = Parent
        self.weight = 480
        self.height = 720
        if(session == None): return
        else: self.__session = session
        QDialog.__init__(self,Parent)
        self.setWindowFlags(Qt.FramelessWindowHint) # removes borders
        self.setAttribute(Qt.WA_TranslucentBackground) # Making it translucent to make a trick with the shadows
        self.setAttribute( Qt.WA_DeleteOnClose) 

    def center(self,parent:QMainWindow): # this function is responsible for centering the modal with respect its father
        qr = self.frameGeometry()
        pr = parent.geometry()
        x = (parent.width() - qr.width()) / 2
        y = (parent.height() - qr.height()) / 2 
        self.setGeometry(x,y,qr.width(),qr.height())

    def exit(self): # this function is responsible to emit a cancelation signal if exit button was clicked
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea cancelar?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.disconnectSignals()
            self.signals.canceled.emit()
            self.close()
            self.deleteLater()
        else:
            pass

    def disconnectSignals(self): # virtual method, that should be implement for each class that inherit
        raise NotImplementedError()
    
    def getAccessToken(self):
        if self.__session != None:
            return self.__session["access_token"]
        else:
            return None

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            point = self.pos() + event.globalPos() - self.dragPos
             # Negative because it has a border for shadow, can be see it at qt designer with the .ui
            if ((point.x() <= -10 or point.x() >= self.__parent.frameSize().width() - self.weight ) or (point.y() <= -10 or point.y() >= self.__parent.frameSize().height() - self.height)) :
                event.ignore()
            else:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()

    def success(self,_x:object): # this function is responsible to emit a success signal, if dialog was success
        self.signals.success.emit(_x)
        self.disconnectSignals()
        self.close()
        self.deleteLater()
    
    def cancel(self):
        self.disconnectSignals()
        self.signals.canceled.emit()
