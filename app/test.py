import PyQt5
from PyQt5.QtWidgets import QComboBox, QStylePainter, QStyleOptionComboBox, QStyle, QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel,QPainter, QPalette, QBrush, QPen, QStaticText, QFont, QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt,QRect, QPoint, QResource, QFile
from uuid import uuid4,UUID
from classes import Logica
from resources import *

class mainWindw(QMainWindow):

    def __init__(self):
        super(mainWindw,self).__init__()
        ad = list([])
        if not type(ad) is list:
            print("no a list")
        else:
            print("is a list")

    #def setupUI(self):
    #    self.setGeometry(250,250,250,250)
    #    self.setWindowTitle("Test")
    #    self.cmb = colorComboBox(self)
    #    self.cmb.setGeometry(125,125,75,25)
    #    pixmap = QPixmap(25,25)
    #    pixmap.fill(QColor("red"))
    #    Icon =  QIcon(pixmap)
    #   self.cmb.addItem(Icon,"red")


if __name__ == "__main__":
    app = QApplication([])
    main = mainWindw()
    app.exec()