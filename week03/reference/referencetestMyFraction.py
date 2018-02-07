#!/usr/bin/env python3
import unittest
from testfixtures import Comparison as C
from MyFraction import MyFraction as Fraction

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
        result = frac1 + frac2
        self.assertEqual("0", str(result))

    def test_addTwoWholeNumbers(self):
        frac1 = Fraction(9)
        frac2 = Fraction(4)
        result = frac1 + frac2
        self.assertEqual("13", str(result))

    def test_addTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 4)
        result = frac1 + frac2
        self.assertEqual("1/2", str(result))

    def test_addTwoFractionsWithDifferentDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 5)
        result = frac1 + frac2
        self.assertEqual("47/15", str(result))

    def test_reduction(self):
        frac = Fraction(6, 4)
        self.assertEqual("3/2", str(frac))

    def test_addTwoFractionsAndReduce(self):
        frac1 = Fraction(4, 4)
        frac2 = Fraction(1, 2)
        result = frac1 + frac2
        self.assertEqual("3/2", str(result))

    def test_addANegativeNumberToAPositiveFraction(self):
        frac1 = Fraction(3, 4)
        frac2 = Fraction(-10, 6)
        result = frac1 + frac2
        self.assertEqual("-11/12", str(result))

    def test_creatingAFractionFromAFloatShouldRaiseTypeError(self):
        with self.assertRaises(TypeError):
            Fraction(4, 3.14)

    def test_subtractTwoFractionsWithDifferentDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 5)
        result = frac1 - frac2
        self.assertEqual("23/15", str(result))

    def test_subtractTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 3)
        result = frac1 - frac2
        self.assertEqual("1", str(result))

    def test_multiplyTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 3)
        result = frac1 * frac2
        self.assertEqual("28/9", str(result))

    def test_divideTwoFractionsWithSameDenominators(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(4, 3)
        result = frac1 / frac2
        self.assertEqual("7/4", str(result))

    def test_divideFractionWithWholeNumber(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(7)
        result = frac1 / frac2
        self.assertEqual("1/3", str(result))

    def test_divideFractionWithZero(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(7, 0)
        with self.assertRaises(ValueError):
            frac1 / frac2

    def test_chainingMultipleOperations(self):
        frac1 = Fraction(7, 3)
        frac2 = Fraction(45, 7)
        frac3 = Fraction(-7, 2)
        frac4 = Fraction(12, 8)
        frac5 = Fraction(4, 9)
        actual = frac1 + frac2 - frac3 * frac4 / frac5
        expected = C(Fraction, numerator=6913, denominator=336)
        self.assertEqual(expected, actual)