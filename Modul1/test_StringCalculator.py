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

    def testIfReturnsSumOfNumbersIfFloatAndIntegerNumbersAreGivenSeparatedByComa(self):
        calculator = StringCalculator()
        self.assertEqual('9.6', calculator.add('2.2', '2.3,1.0,2.1', '2.0'))

    def testIfReturnsSumOfNumbersIfFloatAndIntegerNumbersAreGivenSeparatedByComaOrNl(self):
        calculator = StringCalculator()
        self.assertEqual('9.5', calculator.add('2.2', '2.3\n1.0,2', '2.0'))

    def testIfReturnsErrorMessageWhenDoubledSeparatorFound(self):
        calculator = StringCalculator()
        self.assertEqual("Number expected but \'\\n\' found at position 3.", calculator.add('2.2', '2.3,\n1.0\n,2', '2.0'))

    def testIfReturnsErrorMessageWhenMissingNumberInLastPositionFound(self):
        calculator = StringCalculator()
        self.assertEqual("Number expected but EOF found", calculator.add('2.2', '2.3\n1.0,', '2.0'))

    def testIfReturnsZeroIfEmptyStringIsGiven(self):
        calculator = StringCalculator()
        self.assertEqual('0', calculator.add(''))
