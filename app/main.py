from PyQt5.QtWidgets import QApplication
from forms.LoginForm import UILogin
from forms.MainForm import UIMainWindow

def showMainForm(mainForm:UIMainWindow,session):
    mainForm.session = session
    mainForm.show()

if __name__ == "__main__": # this class only manage the Qapp, includes change from LoginForm to MainForm

    app = QApplication([])
    loginForm = UILogin()
    mainForm = UIMainWindow()
    loginForm.signals.login.connect(lambda _x: showMainForm(mainForm,_x) )
    mainForm.signals.logout.connect(lambda: loginForm.show())
    loginForm,mainForm.signals.finish.connect(lambda: app.closeAllWindows())
    loginForm.show()
    app.exec_()


