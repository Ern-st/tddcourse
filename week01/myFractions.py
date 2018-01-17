#!/usr/bin/env python3

class MyFraction:

    def __init__(self, fractionString):
        self.numerator, self.denominator = [ int(x) for x in fractionString.split("/") ]

    def getWholeNumber(self):
        return int(self.numerator / self.denominator)

    def add(self, addend):
        return 1