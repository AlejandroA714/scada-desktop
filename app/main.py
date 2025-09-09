import sys
from PyQt5.QtWidgets import QApplication
from forms import UILogin, UIMainWindow
from classes import logger,timer,session
from functools import partial
from notificator import notificator
from notificator.alingments import TopRight
from PyQt5.QtGui import QFontDatabase
from resources import *
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = os.path.join(os.path.expanduser("~"), ".scada_logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_PATH = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

fh = RotatingFileHandler(LOG_PATH, maxBytes=2_000_000, backupCount=5, encoding="utf-8")
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
logging.getLogger().addHandler(fh)

def excepthook(exc_type, exc, tb):
    logging.exception("Excepción no manejada", exc_info=(exc_type, exc, tb))
    # (opcional) no mates la app: NO llames a sys.__excepthook__
    # Puedes mostrar algo breve con QMessageBox si ya hay QApplication
sys.excepthook = excepthook
class application(QApplication):

    def __init__(self,*args):
        super(application,self).__init__(*args)
        self.mainWindow = None
        self.timer = timer() # Initializate timer
        self.logger = logger() # Initializate logger
        self.importFonts()

    def showLoginForm(self,sessionClosed = False,timerid = 0):
        if sessionClosed:
            self.mainWindow.signals.logout.disconnect()
            session().destroy()
            self.timer.restartTimer(timerid)
            self.mainWindow.deleteLater()
            self.processEvents()
            noft = notificator()
            noft.info("¡Información!","Sesion Finalizada con exito",None,TopRight)
        self.mainWindow = UILogin()
        self.mainWindow.signals.login.connect(self.showMainForm)
        self.mainWindow.signals.finish.connect(self.exit)
        self.mainWindow.show()

    def showMainForm(self,s):
        session(s)
        self.mainWindow.signals.login.disconnect(self.showMainForm)
        self.mainWindow.signals.finish.disconnect(self.exit)
        self.mainWindow.deleteLater()
        self.processEvents()
        self.mainWindow = UIMainWindow()
        self.mainWindow.show()
        timerid = self.timer.startTimer(1000)
        self.mainWindow.signals.logout.connect(partial(self.showLoginForm,True,timerid))

    def importFonts(self):
        """ Import all roboto fonts to be used at application """
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Black.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-BlackItalic.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Bold.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-BoldItalic.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Italic.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-LightItalic.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Medium.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-MediumItalic.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Regular.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-Thin.ttf")
        QFontDatabase.addApplicationFont(":/source/fonts/Roboto-ThinItalic.ttf")

if __name__ == "__main__":
    app = application([])
    app.showLoginForm()
    app.exec()
    