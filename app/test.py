from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

class Window(QWidget):
    @profile
    def __init__(self,*args):
        QWidget.__init__(self)
        self.checkbox = QCheckBox('Delete')
        self.button = QPushButton('Open', self)
        self.button.clicked.connect(self.openDialog)
        layout = QHBoxLayout(self)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)

    @profile
    def openDialog(self,*args):
        widget = QDialog(self)
        if (self.checkbox.isChecked() and
            not widget.testAttribute(QtCore.Qt.WA_DeleteOnClose)):
            widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            for child in self.findChildren(QDialog):
                if child is not widget:
                    child.deleteLater()
        label = QLabel(widget)
        button = QPushButton('Close', widget)
        button.clicked.connect(widget.close)
        layout = QVBoxLayout(widget)
        layout.addWidget(label)
        layout.addWidget(button)
        objects = self.findChildren(QtCore.QObject)
        label.setText('Objects = %d' % len(objects))
        print(objects)
        widget.show()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 100, 50)
    window.show()
    sys.exit(app.exec_())