from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from classes.widget import widget
from resources.resources import *


class UIWidgetP(widget):

    def __init__(self,y):
        super(UIWidgetP,self).__init__()
        self.setupUi(y)

    def setupUi(self,y):
        Form = self
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(376, 88)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProjectFrame = QtWidgets.QFrame(Form)
        self.ProjectFrame.setGeometry(QtCore.QRect(0, y, 377, 91))
        self.ProjectFrame.setMaximumSize(QtCore.QSize(16777215, 91))
        self.ProjectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProjectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProjectFrame.setObjectName("ProjectFrame")
        self.lblCount = QtWidgets.QLabel(self.ProjectFrame)
        self.lblCount.setGeometry(QtCore.QRect(10, 60, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCount.setFont(font)
        self.lblCount.setObjectName("lblCount")
        self.ProjectTitle = QtWidgets.QTextBrowser(self.ProjectFrame)
        self.ProjectTitle.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.ProjectTitle.setMaximumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ProjectTitle.setFont(font)
        self.ProjectTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProjectTitle.setLineWidth(0)
        self.ProjectTitle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ProjectTitle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ProjectTitle.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ProjectTitle.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.ProjectTitle.setDocumentTitle("")
        self.ProjectTitle.setOverwriteMode(False)
        self.ProjectTitle.setAcceptRichText(True)
        self.ProjectTitle.setOpenLinks(False)
        self.ProjectTitle.setObjectName("ProjectTitle")
        self.btnAbrir = QtWidgets.QPushButton(self.ProjectFrame)
        self.btnAbrir.setGeometry(QtCore.QRect(270, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAbrir.setFont(font)
        self.btnAbrir.setStyleSheet("border: 1px solid green;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/Abrir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbrir.setIcon(icon)
        self.btnAbrir.setFlat(True)
        self.btnAbrir.setObjectName("btnAbrir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblCount.setText(_translate("Form", "Contiene 1 Controlador"))
        self.ProjectTitle.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Proyecto 1</span></p></body></html>"))
        self.btnAbrir.setText(_translate("Form", "Abrir"))
