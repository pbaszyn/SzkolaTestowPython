from unittest import TestCase
from StringCalculator import StringCalculator


class TestStringCalculator(TestCase):

    def testIfReturnsNumberIfNumberIsGiven(self):
        calculator = StringCalculator()
        self.assertEqual('4', calculator.add('4'))

    def testIfReturnsSumOfNumbersIfTwoNumbersAreGiven(self):
        calculator = StringCalculator()
        self.assertEqual('4', calculator.add('2.0', '2'))

    def testIfReturnsSumOfNumbersIfTwoFloatNumbersAreGiven(self):
        calculator = StringCalculator()
        self.assertEqual('4.5', calculator.add('2.2', '2.3'))

    def testIfReturnsSumOfNumbersIfFourFloatAndIntegerNumbersAreGiven(self):
        calculator = StringCalculator()
        self.assertEqual('7.5', calculator.add('2.2', '2.3', '1', '2.0'))

    def testIfReturnsZeroIfEmptyStringIsGiven(self):
        calculator = StringCalculator()
        self.assertEqual('0', calculator.add(''))
