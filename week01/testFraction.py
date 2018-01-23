#!/usr/bin/env python3
import unittest
from myFractions import MyFraction as Fraction

class TestFractions(unittest.TestCase):

    def test_fractionFromString(self):
        fraction = Fraction.fromString("2/2")
        self.assertEqual(1, fraction.getWholeNumber())

    def test_isEqual(self):
        fraction = Fraction(3, 3)
        self.assertEqual(1, fraction.getWholeNumber())

    def test_addTwoZeroFractions(self):
        frac1 = Fraction(0, 4)
        frac2 = Fraction(0, 20)
        result = frac1.add(frac2)
        self.assertEqual("0/0", str(result))

    def test_addTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 4)
        result = frac1.add(frac2)
        self.assertEqual("1/2", str(result))

    def test_addTwoFractionsWithDifferentDenominators(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 2)
        result = frac1.add(frac2)
        self.assertEqual("3/4", str(result))

    def test_reduction(self):
        frac = Fraction(6, 4)
        self.assertEqual("3/2", str(frac))

    def test_addTwoFractionsAndReduce(self):
        frac1 = Fraction(4, 4)
        frac2 = Fraction(1, 2)
        result = frac1.add(frac2)
        self.assertEqual("3/2", str(result))

    def test_toString(self):
        frac = Fraction(2, 7)
        self.assertEqual("2/7", str(frac))

    # def test_addTwoWholeNumbers(self):
    #     frac1 = Fraction(4)
    #     frac2 = Fraction(9)
    #     self.assertEqual(13, frac1.add(frac2))
