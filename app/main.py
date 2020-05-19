import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from forms.LoginForm import UILogin
from forms.MainForm import UIMainWindow
from resources.resources import *

class MainWindow(QMainWindow,UIMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)        
        self.setWindowIcon(QIcon(':/source/img/if_16_1751363.ico'))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
