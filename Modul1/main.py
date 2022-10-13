from StringCalculator import StringCalculator


def isequal(expected, actual, message):
    if expected == actual:
        return message + ' - passed'
    else:
        return message + ' - failed'


calculator = StringCalculator()
print(isequal('4', calculator.add('2', '2'), 'Calculator should return sum of numbers given'))
print(isequal('4', calculator.add('2', '3'), 'Calculator should return sum of numbers given'))
print(isequal('0', calculator.add(''), 'Calculator should return zero when is no arguments'))
