from PyQt5.QtWidgets import QApplication
from forms import UILogin, UIMainWindow
from classes import logger,timer,session
from functools import partial
from notificator import notificator
from notificator.alingments import TopRight
from PyQt5.QtGui import QFontDatabase
from resources import *

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
    