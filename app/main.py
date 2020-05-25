from PyQt5.QtWidgets import QApplication
from forms.Windows.LoginForm import UILogin
from forms.Windows.MainForm import UIMainWindow
from classes.utils.timer import timer
from classes.utils.logger import logger

class application(QApplication):

    def __init__(self,*args):
        super(application,self).__init__(*args)
        self.__mainForm = UIMainWindow()
        self.__loginForm = UILogin()
        self.__timer = timer() # Initializate timer
        self.__logger = logger() # Initializate logger
        self.connectSignals() # connects the signal to be captured
        self.__loginForm.show()

    def connectSignals(self):
        self.__loginForm.signals.login.connect(self.showMainForm)
        self.__mainForm.signals.logout.connect(lambda : self.__loginForm.show())
        self.__loginForm.signals.finish.connect(lambda: app.closeAllWindows())

    def showMainForm(self,session):
        self.__mainForm.session = session
        self.__mainForm.show()
        self.__timer.startTimer(1000)

if __name__ == "__main__":
    app = application([])
    app.exec_()