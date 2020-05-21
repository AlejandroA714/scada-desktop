from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal

class widgetSignals(QObject):
    sucess = pyqtSignal()

class widget(QWidget):

    signals = widgetSignals()
    
    def __init__(self):
        QWidget.__init__(self)


