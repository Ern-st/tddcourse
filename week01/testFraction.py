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
        frac1 = Fraction(0, 0)
        frac2 = Fraction(0, 0)
        result = frac1.add(frac2)
        self.assertEqual("0/0", str(result))

    def test_addTwoFractions(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 2)
        result = frac1.add(frac2)
        self.assertEqual("3/4", str(result))

    def test_toString(self):
        frac = Fraction(2, 7)
        self.assertEqual("2/7", str(frac))

    # def test_lowestTerms(self):
    #     frac = Fraction.fromString("4/6")
    #     self.assertEqual("2/3", frac)

    # def test_addTwoWholeNumbers(self):
    #     frac1 = Fraction(4)
    #     frac2 = Fraction(9)
    #     self.assertEqual(13, frac1.add(frac2))
