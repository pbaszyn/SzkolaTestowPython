from unittest import TestCase
from StringCalculator import StringCalculator


class TestStringCalculator(TestCase):

    def testIfReturnsNumberIfNumberIsGiven(self):
        calculator = StringCalculator()
        self.assertEqual('4', calculator.add('4'))

    def testIfReturnsSumOfNumbersIfTwoNumbersAreGiven(self):
        calculator = StringCalculator()
        self.assertEqual('4', calculator.add('2', '2'))

    def testIfReturnsZeroIfEmptyStringIsGiven(self):
        calculator = StringCalculator()
        self.assertEqual('0', calculator.add(''))
