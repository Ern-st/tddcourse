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


    def test_addTwoFractions(self):
        frac1 = Fraction(2, 4)
        frac2 = Fraction(1, 2)
        self.assertEqual(1, frac1.add(frac2))
