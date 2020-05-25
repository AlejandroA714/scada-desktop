from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from classes.objects.time import time

class timerSignals(QObject):
    
    timeout = pyqtSignal()
    access_token_expired = pyqtSignal()
    session_expired = pyqtSignal()

class timer(QTimer):

    signals =  timerSignals()
    __instance = None # Instance of the timer; just can exists one on all the app
  
    def timerEvent(self,event):
        self.__time.addSeconds(1)
        print(self.__time.__dict__)
        if self.__time.hours == 23:
            self.signals.access_token_expired.emit()
        self.signals.timeout.emit()

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  QTimer.__new__(cls) 
            super(timer,cls.__instance).__init__()
            cls.__time = time()     
        return cls.__instance

