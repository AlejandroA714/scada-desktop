from classes import device, timer, timerSignals
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal

class clase(QObject):

    def __init__(self):
        self.__private = 0
        back =  self.__private
        self.__private = 1
        print(self.__private)
        print(back)

    def second(self):
        print("one second")

    def countSlots(self):   
        pass

c = clase()

