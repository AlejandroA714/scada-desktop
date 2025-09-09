from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, QThreadPool, QThread
from ..utils.session import session
from functools import partial

class widgetSignals(QObject):

    sucess = pyqtSignal(object)
    edit = pyqtSignal(object)
    delete = pyqtSignal(object)
    copy = pyqtSignal(object)
    enable = pyqtSignal(object)
    disable = pyqtSignal(object)

class widget(QWidget):

    threadpool = QThreadPool()

    def __init__(self,Parent=None):
        self.Parent = Parent
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
            self.signals.sucess.disconnect()
            self.close()
        else:
            pass
    def register_thread(self, t: QThread):
        if not hasattr(self, "_threads"):
          self._threads = set()
        self._threads.add(t)

    def stop_threads(self, timeout_ms=2000):
        for t in list(self._threads):
            if t.isRunning():
                t.requestInterruption()
                t.quit()
                t.wait(timeout_ms)
        self._threads.clear()

    def edit(self,tilte:str,text:str):
        reply = self.prompt(tilte,text)
        if reply == QMessageBox.Yes:
            self.signals.edit.emit(self.variable)

    def delete(self,title:str,text:str):
        reply = self.prompt(title,text)
        if reply == QMessageBox.Yes:
            self.signals.delete.emit(self.variable)

    def close(self):
        super().close()
        self.disconnectSignals()
        #self.stop_threads()
        if hasattr(self,'worker'): # if attribute worker is defined then, there is a thread execution pending
            self.worker.signals.finished.disconnect() # disconnect signal from the worker
            self.worker.terminate() # ask to end the execution of the thread
            self.worker.wait()
        self.deleteLater()
        QApplication.processEvents()

    def disconnectSignals(self):
        raise NotImplementedError

    def disconnectSuccess(self,handler):
        self.signals.sucess.disconnect(handler)
    def disconnectEdit(self,handler):
        self.signals.edit.disconnect(handler)
    def disconnectDelete(self,handler):
        self.signals.delete.disconnect(handler)

    def prompt(self,title,text):
        reply = QMessageBox.question(
            self, title,
            text,
            QMessageBox.Yes | QMessageBox.No)
        return reply
