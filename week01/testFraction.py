#!/usr/bin/env python3
import unittest
from myFractions import MyFraction as Fraction

class TestFractions(unittest.TestCase):

    def test_isEqual(self):
        fraction = Fraction("3/3")
        print(fraction.getWholeNumber())
        self.assertEqual(1, fraction.getWholeNumber())

    def test_isNotEqual(self):
        self.assertNotEqual(1, 2)

    def test_addTwoFractions(self):
        frac1 = Fraction("2/4")
        frac2 = Fraction("1/2")
        self.assertEqual(1, frac1.add(frac2))
