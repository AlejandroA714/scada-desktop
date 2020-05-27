import sys, traceback, logging, os
from classes.utils.logger import logger
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QApplication
from requests.exceptions import HTTPError

#This file handle the execute of thread to contact with API SCADA
# wiil call and request executing a thread to avoid program freezing

class WorkerSignals(QObject): # Class to emit signals at execute a thread

    finished = pyqtSignal() # returns no data
    error = pyqtSignal(Exception) # return a tuple with error
    result = pyqtSignal(object) # if success return data, json object
    #progress = pyqtSignal(int) # returns an int with progress, not should be used

class Worker(QRunnable): # Class to execute a function inside a thread

    def __init__(self,fn,*args,**kwargs): # fn:  Function to be executed

        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals() 
        self.logger = logger()
        #self.kwargs['progress_callback'] = self.signals.progress 

    @pyqtSlot()
    def run(self):   
        # Retrieve args/kwargs here; and processing using them
        try:
            result = self.fn(*self.args, **self.kwargs) #Execute function, passing args and kwargs, always recibe **kwargs as json object
        except Exception as e:
            self.logger.log_error(e)
            if isinstance(e,HTTPError):#
                if e.response.status_code == 401:
                    QMessageBox.warning(None,"¡Error!","Sesión expirada\nCerrando Aplicación")
                    QApplication.exit()
            traceback.print_exc()
            self.signals.error.emit(e)   
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

