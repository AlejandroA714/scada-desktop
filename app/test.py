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
        self.setupUI()
        colors = {"aqua","aquamarine","beige","black","blue","blueviolet","brown","burlywood","chartreuse",
            "cadetblue","chocolate","crimson","cyan","darkblue","fuchsia","gold","gray",
            "green","greenyellow","hotpink","indigo","lime","magenta","navy","olive",
            "orange","orangered","orchid","palegreen","purple","red","salmon","silver",
            "skyblue","slateblue","springgreen","tomato","turquoise","violet","wheat","yellow","yellowgreen"}

        for color in colors:
            print(color)
            pixmap = QPixmap(25,25)
            pixmap.fill(QColor(color))
            Icon = QIcon(pixmap)
            self.cmb.addItem(Icon,color)
        #ad = list([])
        #if not type(ad) is list:
        #    print("no a list")
        #else:
        #    print("is a list")
        #Logica.AbrirProyectoDebug(**{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTIyNTQyNTQsIm5iZiI6MTU5MjI1NDI1NCwianRpIjoiMTdhNTNjNWEtM2Y3ZS00YjU4LTg3YzktZTYwM2ZhMzlhYjE4IiwiZXhwIjoxNTkyMzQwNjU0LCJpZGVudGl0eSI6eyJJZCI6IjVkYTlmOWIxZWYyOGJkMjEyMDkxMGI0ZSIsIlVzdWFyaW8iOiJhZG1pbmlzdHJhZG9yLnNjYWRhIiwiVGlwbyI6IkFkbWluaXN0cmFkb3IifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIiwidXNlcl9jbGFpbXMiOnsiVGlwbyI6IkFkbWluaXN0cmFkb3IiLCJJZCI6IjVkYTlmOWIxZWYyOGJkMjEyMDkxMGI0ZSJ9fQ.7J0c0rgWRN_4O-tvcIqlWqt3OwvFEZuZVqWlCYB8780"})
    def setupUI(self):
        self.setGeometry(250,250,250,250)
        self.setWindowTitle("Test")
        self.cmb = QComboBox(self)
        self.cmb.setGeometry(125,125,75,25)
    #    pixmap = QPixmap(25,25)
    #    pixmap.fill(QColor("red"))
    #    Icon =  QIcon(pixmap)
    #   self.cmb.addItem(Icon,"red")


if __name__ == "__main__":
    app = QApplication([])
    main = mainWindw()
    main.show()
    app.exec()