import PyQt5
from PyQt5.QtWidgets import QComboBox, QStylePainter, QStyleOptionComboBox, QStyle, QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel,QPainter, QPalette, QBrush, QPen, QStaticText, QFont
from PyQt5.QtCore import Qt,QRect, QPoint
from forms import colorComboBox

class mainWindw(QMainWindow):

    def __init__(self):
        super(mainWindw,self).__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setGeometry(250,250,250,250)
        self.setWindowTitle("Test")
        self.cmb = colorComboBox(self)
        self.cmb.setGeometry(125,125,75,25)
        self.cmb.addItem("item 1")
        self.cmb.addItem("item 2")

    #def paintEvent(self,ev):
        #painter = QPainter(self)
        #painter.setPen(QPen(Qt.black,Qt.SolidLine))
        #painter.setFont(QFont("Roboto",11,1,False))
        #painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))
        #painter.drawStaticText(QPoint(0,0),QStaticText("aqua"))
        #painter.drawRect(QRect(35,0,12,12))

    def drawItem(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    main = mainWindw()
    app.exec()