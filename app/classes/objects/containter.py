class container(object):

    def __init__(self,dict):
        self.tab = dict["tab"]
        self.workSpace = dict["workSpace"]
        

    @property
    def tab(self):
        return self.__tab

    @tab.setter
    def tab(self,value):
        self.__tab = value

    @property
    def workSpace(self):
        return self.__workSpace

    @workSpace.setter
    def workSpace(self,value):
        self.__workSpace = value