import sys, traceback, logging, os
from classes.utils.logger import logger
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QMessageBox, QApplication
from requests.exceptions import HTTPError, ConnectionError

#This file handle the execute of thread to contact with API SCADA
# will call and request executing a thread to avoid program freezing

class WorkerSignals(QObject): # Class to emit signals at execute a thread

    finished = pyqtSignal(object) # returns data, json object
    error = pyqtSignal(Exception) # return a tuple with error
    result = pyqtSignal(object) # if success return data, json object

class Worker(QThread): # Class to execute a function inside a thread

    def __init__(self,fn,*args,Parent=None,**kwargs): # fn:  Function to be executed

        super().__init__(Parent)
        self.__running = False
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals() 
        self.logger = logger()
        #self.setAutoDelete(True)

    @pyqtSlot()
    def run(self):   
        # Retrieve args/kwargs here; and processing using them
        self.__running = True
        try:
            result = self.fn(*self.args, **self.kwargs) #Execute function, passing args and kwargs, always recibe **kwargs as json object
            self.signals.finished.emit(result)
        except Exception as e:
            self.logger.log_error(e)
            if isinstance(e,HTTPError): # Receives an unathorized 
                if e.response.status_code == 401:
                    QMessageBox.warning(None,"¡Error!","Sesión expirada o Invalida\nCerrando Aplicación")
                    QApplication.exit()
            if isinstance(e,ConnectionError):
                e = Exception("Fallo al conectar con el servicio SCADA")
            traceback.print_exc()
            self.signals.finished.emit(e) # Returns an object exception

