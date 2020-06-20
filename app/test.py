from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction
from PyQt5 import QtWidgets,QtCore

class app(QApplication):

    def __init__(self):
        super(app,self).__init__([])

class form(QMainWindow):
    def __init__(self):
        super(form,self).__init__()
        self.setupUI()

    def setupUI(self):
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 740)
        MainWindow.setMinimumSize(QtCore.QSize(840, 740))

        self.MenuArchivo = QtWidgets.QToolButton(self)
        self.MenuArchivo.setGeometry(QtCore.QRect(0, 0, 71, 24))
        self.MenuArchivo.setStyleSheet("margin:0px;")
        self.MenuArchivo.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuArchivo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuArchivo.setAutoRaise(True)
        self.MenuArchivo.setArrowType(QtCore.Qt.NoArrow)
        self.MenuArchivo.setObjectName("MenuArchivo")

        self.defineMenuArchivo()

    def defineMenuArchivo(self):
        # Definicion de menus
        configuracionesMenu = QMenu()
        configuracionesMenu.addAction("{:15s}{:>12s}".format("Configuraciones","Ctrl+C"),self.new_Callback)
        configuracionesMenu.addAction("{:15s}{:>17s}".format("Dispostivos","Ctrl+D"),self.new_Callback)
        configuracionesMenu.addAction("{:15s}{:>19s}".format("API Local","Ctrl+H"),self.new_Callback)
        configuracionesMenu.addAction("{:15s}{:>19s}".format("Usuarios","Ctrl+U"),self.new_Callback)
        configuracionesMenu.addAction("{:15s}{:>20s}".format("Cuenta","Ctrl+P"),self.new_Callback)
        configuracionesMenu.addAction("{:15s}{:>20s}".format("Acerca de",""), self.new_Callback)

        self.MenuArchivo.setMenu(configuracionesMenu)
        defaultAction = QAction("Dispositivos",self)
        defaultAction.triggered.connect(self.new_Callback)
        self.MenuArchivo.setDefaultAction(defaultAction)

    def new_Callback(self):
        print("called nuevo")
    
    def open_Callback(self):
        print("called open")
    
    def delete_Callback(self):
        print("called delete")

application = app()
window = form()
window.show()
application.exec()




