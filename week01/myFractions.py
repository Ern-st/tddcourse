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
        return cls(numerator, denominator)

    def __highestCommonFactor(self, a, b):
        if b == 0:
            return a
        return self.__highestCommonFactor(b, a%b)

    def __leastCommonMultiple(self, a,b):
        return int(a*b / self.__highestCommonFactor(a,b))

    def __commonDenominator(self, frac1, frac2):
        if frac1.denominator != frac2.denominator:
            commonDenominator   = self.__leastCommonMultiple(frac1.denominator, frac2.denominator)
            frac1.numerator     = int(frac1.numerator * (commonDenominator / frac1.denominator))
            frac1.denominator   = commonDenominator
            frac2.numerator     = int(frac2.numerator * (commonDenominator / frac2.denominator))
            frac2.denominator   = commonDenominator
        return frac1, frac2

    def __lowestTerms(self, numerator, denominator):
        if numerator == 0:
            return MyFraction(numerator, 0)
        lowestTerm = self.__highestCommonFactor(numerator, denominator)
        return MyFraction(
            int(numerator / lowestTerm),
            int(denominator / lowestTerm)
        )

    def getWholeNumber(self):
        return int(self.numerator / self.denominator)

    def add(self, addend):
        frac1, frac2 = self.__commonDenominator(self, addend)
        result = frac1.numerator + frac2.numerator
        result = self.__lowestTerms(result, frac1.denominator)
        return result