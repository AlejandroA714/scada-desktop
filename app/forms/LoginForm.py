from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QDesktopWidget,QMessageBox, QApplication
from resources.resources import *
from classes.logica import Logica
from classes.worker import Worker
from forms.MainForm import UIMainWindow

#
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
class UILogin(object):
    
    threadpool = QThreadPool()

    def setupUi(self, Login):
        #self.setWindowFlags(Qt.FramelessWindowHint)
        Login.setObjectName("Login")
        Login.resize(406, 528)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        Login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView = QtWidgets.QGraphicsView(Login)
        self.graphicsView.setGeometry(QtCore.QRect(0, -10, 406, 116))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(10, 5, 81, 101))
        self.label.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 110, 45))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 71, 71))
        self.label_3.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(40, 180, 321, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 41, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/source/img/Usuario.png"))
        self.label_6.setObjectName("label_6")
        self.txtUsuario = QtWidgets.QLineEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(100, 70, 141, 21))
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtUsuario.setPlaceholderText("administrador.scada")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 110, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/source/img/Password.png"))
        self.label_7.setObjectName("label_7")
        self.txtPassword = QtWidgets.QLineEdit(self.frame)
        self.txtPassword.setGeometry(QtCore.QRect(100, 130, 141, 21))
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setPlaceholderText("**********")
        self.btnAceptar = QtWidgets.QPushButton(self.frame)
        self.btnAceptar.setGeometry(QtCore.QRect(90, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("border:1px solid green;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar.setIcon(icon1)
        self.btnAceptar.setIconSize(QtCore.QSize(24, 24))
        self.btnAceptar.setShortcut("")
        self.btnAceptar.setCheckable(False)
        self.btnAceptar.setFlat(True)
        self.btnAceptar.setObjectName("btnAceptar")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 190, 161, 16))
        self.label_8.setOpenExternalLinks(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel#label_8{color: rgb(0, 0, 255); }QLabel:hover#label_8{color:rg(0,0,150);}")
        self.label_8.setObjectName("label_8")
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5 = QtWidgets.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnExit = QtWidgets.QPushButton(Login)
        self.btnExit.setGeometry(QtCore.QRect(375, 0, 32, 32))
        self.btnExit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon2)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(Login)
        self.center()
        
        QtCore.QMetaObject.connectSlotsByName(Login)


        self.movie = QMovie(":/source/img/Cargando.gif") # 80 ,200
        self.lblmovie = QtWidgets.QLabel(self.frame)
        self.lblmovie.setGeometry(QtCore.QRect(135, 235,48,48))
        self.lblmovie.setMovie(self.movie)
        self.lblmovie.hide()
        self.movie.setScaledSize(QtCore.QSize(48,48))

        # listener

        self.btnAceptar.clicked.connect(self.btnAceptar_Click)
        self.btnExit.clicked.connect(self.exit)
        
        # end

    def exit(self):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea salir?",
            QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.exit()
        else:
            pass
    
    def btnAceptar_Click(self):
        if(self.txtUsuario.text() == "" or self.txtPassword.text() == ""):
            QMessageBox.warning(self,"¡Advertencia!","Rellene los campos solicitados")
            self.lblmovie.hide()
            self.btnAceptar.show()
            return
        self.btnAceptar.hide()
        self.lblmovie.show()
        self.movie.start()
        worker = Worker(Logica.IniciarSesion,**{"Usuario":self.txtUsuario.text(),"Password":self.txtPassword.text()})
        worker.signals.result.connect(self.btnAceptar_CallBack)
        worker.signals.error.connect(self.btnAceptar_CallBack)
        self.threadpool.start(worker)

    def btnAceptar_CallBack(self,s):
        self.lblmovie.hide()
        self.btnAceptar.show()
        if isinstance(s,Exception):
            self.lblmovie.hide()
            self.btnAceptar.show()
            QMessageBox.information(self,"¡Error!", "¡Error! %s" % str(s))
            return
        self.lblmovie.hide()
        self.btnAceptar.show()
        if(s["Id"] is None): # If returns None, API is online, but mongodb isnt
            QMessageBox.warning(self,"¡Error!", "No se pudo iniciar sesion")
            return
        if(s["Id"] == ""): # If returns an empty string, credentials are bad
            QMessageBox.warning(self,"¡Error!", "Usuario y/o contraseña incorrectos")
            return
        if(s["Id"] != "" and s["Enabled"] == False): # If Enabled is false, then cannot login
            QMessageBox.warning(self,"¡Advertencia!", "Usuario no tiene permitido iniciar sesion")
            return
        
        main = UIMainWindow()
        main.setupUi(self)
    
           
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Sistema SCADA"))
        self.label_2.setText(_translate("Login", "SCADA"))
        self.label_4.setText(_translate("Login", "Iniciar Sesiòn"))
        self.btnAceptar.setText(_translate("Login", "Iniciar Sesion"))
        self.label_8.setText(_translate("Login", "¿Olvidaste tu contraseña?"))
        self.label_5.setText(_translate("Login", "Credenciales"))
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())