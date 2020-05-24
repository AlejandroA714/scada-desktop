from PyQt5.QtCore import QTimer, pyqtSignal, QObject

class timerSignals(QObject):
    
    timeout = pyqtSignal()

class timer(QTimer):

    signals =  timerSignals()
    __instance = None # only can exists 1 instance; Singleton concept

    def __init__(self ):
        self.i = 0
        QTimer.__init__(self)
        self.startTimer(1000)

    def timerEvent(self,event):
        self.i = self.i + 1
        print(self.i)
        self.signals.timeout.emit()

    def __new__(cls,*args,**kwargs ):
        if cls.__instance is None :
            cls.__instance =  QTimer.__new__(cls,*args,**kwargs)
        return cls.__instance


