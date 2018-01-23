#!/usr/bin/env python3

class MyFraction:

    def __init__(self, numerator, denominator = 1):
        if type(numerator) is not int or type(denominator) is not int:
            raise(TypeError("You can only use Integers for MyFractions or strings with the 'fromString' method"))
        lowestTerm = self.__lowestTerms(numerator, denominator)
        self.numerator = lowestTerm['numerator']
        self.denominator = lowestTerm['denominator']

    def __str__(self):
        if self.numerator == 0 or self.denominator == 0:
            return "0"
        elif self.numerator % self.denominator == 0:
            return "{0}".format(int(self.numerator / self.denominator))
        else:
            return "{0}/{1}".format(self.numerator, self.denominator)

    def __repr__(self):
        return "myFraction({0}, {1})".format(self.numerator, self.denominator)

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
            return {'numerator': 0, 'denominator': 0}
        lowestTerm = self.__highestCommonFactor(numerator, denominator)
        return  {
            'numerator': int(numerator / lowestTerm), 
            'denominator': int(denominator / lowestTerm)
            }

    def add(self, addend):
        frac1, frac2 = self.__commonDenominator(self, addend)
        result = frac1.numerator + frac2.numerator
        lowestTerm = self.__lowestTerms(result, frac1.denominator)
        return MyFraction(lowestTerm['numerator'], lowestTerm['denominator'])

    def subtract(self, subtractee):
        frac1, frac2 = self.__commonDenominator(self, subtractee)
        result = frac1.numerator - frac2.numerator
        lowestTerm = self.__lowestTerms(result, frac1.denominator)
        return MyFraction(lowestTerm['numerator'], lowestTerm['denominator'])