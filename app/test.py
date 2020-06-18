from classes import device, variable
from copy import copy

class A:

    def over(self):
        print("super method called")

    def callover(self):
        self.over()

class B(A):
    
    def over(self):
        super().over()
        print("children called")


b = B()
b.callover()