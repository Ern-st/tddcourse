#!/usr/bin/env python3

class MyFraction:

    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    @classmethod
    def fromString(cls, fractionString):
        numerator, denominator = [ int(x) for x in fractionString.split("/") ]
        #print("num: {0} den: {1} input:{2}".format(numerator, denominator, fractionString))
        return cls(numerator, denominator)

    def getWholeNumber(self):
        return int(self.numerator / self.denominator)

    def add(self, addend):
        #compare denominators
        if self.denominator != addend.denominator:
            #do some calc here to find the lowest common denominator
            pass
        result = self.numerator + addend.numerator
        return MyFraction(result, self.denominator)