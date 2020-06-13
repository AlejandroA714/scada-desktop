import PyQt5
from PyQt5.QtWidgets import QComboBox, QStylePainter, QStyleOptionComboBox, QStyle, QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel,QPainter, QPalette, QBrush, QPen, QStaticText, QFont
from PyQt5.QtCore import Qt,QRect, QPoint
from PyQt5.QtCore import Qt,QRect

class colorComboBox(QComboBox):

    def __init__(self,parent):
        super(colorComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def item_checked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked

    def check_items(self):
        checkedItems = []
        for i in range(self.count()):
            if self.item_checked(i):
                checkedItems.append(self.model().item(i, 0).text())
        return checkedItems

    """ def paintEvent(self, event):
        painter = QStylePainter(self)
        #painter.setPen(self.palette().color(QPalette.Text))
        painter.setPen(QPen(Qt.black,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))
        painter.drawStaticText(QPoint(0,0),QStaticText("aqua"))
        painter.drawRect(QRect(25,25,12,12))
        opt = QStyleOptionComboBox()
        self.initStyleOption(opt)
        #opt.currentText = ",".join(self.check_items())
        painter.drawComplexControl(QStyle.CC_ComboBox, opt)
        painter.drawControl(QStyle.CE_ComboBoxLabel, opt) """

    def drawItem(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green,Qt.SolidPattern))
        painter.drawStaticText(0,0,"aqua")
        painter.drawRect(QRect(25,25,12,12))
