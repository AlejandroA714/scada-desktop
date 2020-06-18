from classes import device
from copy import copy

dev = device()

def test(dev):
    print(dev)

test(copy(dev))
print(dev)
