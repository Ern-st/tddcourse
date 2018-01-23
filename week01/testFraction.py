#!/usr/bin/env python3
import unittest
from myFractions import MyFraction as Fraction

class TestFractions(unittest.TestCase):

    def test_fractionFromString(self):
        fraction = Fraction.fromString("2/2")
        self.assertEqual("1", str(fraction))

    def test_toString(self):
        frac = Fraction(2, 7)
        self.assertEqual("2/7", str(frac))

    def test_isEqual(self):
        fraction = Fraction(3, 3)
        self.assertEqual("1", str(fraction))

    def test_addTwoZeroFractions(self):
        frac1 = Fraction(0, 4)
        frac2 = Fraction(0, 0)
        result = frac1.add(frac2)
        self.assertEqual("0", str(result))

    def test_addTwoWholeNumbers(self):
        frac1 = Fraction(9)
        frac2 = Fraction(4)
        result = frac1.add(frac2)
        self.assertEqual("13", str(result))

    def test_addTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 4)
        result = frac1.add(frac2)
        self.assertEqual("1/2", str(result))

    def test_addTwoFractionsWithDifferentDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 5)
        result = frac1.add(frac2)
        self.assertEqual("47/15", str(result))

    def test_reduction(self):
        frac = Fraction(6, 4)
        self.assertEqual("3/2", str(frac))

    def test_addTwoFractionsAndReduce(self):
        frac1 = Fraction(4, 4)
        frac2 = Fraction(1, 2)
        result = frac1.add(frac2)
        self.assertEqual("3/2", str(result))

    def test_addANegativeNumberToAPositiveFraction(self):
        frac1 = Fraction(3, 4)
        frac2 = Fraction(-10, 6)
        result = frac1.add(frac2)
        self.assertEqual("-11/12", str(result))

    def test_creatingAFractionFromAFloat(self):
        with self.assertRaises(TypeError):
            frac = Fraction(4, 3.14)

    def test_subtractTwoFractionsWithDifferentDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 5)
        result = frac1.subtract(frac2)
        self.assertEqual("23/15", str(result))

    def test_subtractTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 3)
        result = frac1.subtract(frac2)
        self.assertEqual("1", str(result))

    def test_multiplyTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 3)
        result = frac1.multiply(frac2)
        self.assertEqual("28/9", str(result))