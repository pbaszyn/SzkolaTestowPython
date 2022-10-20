import math


class StringCalculator:
    def add(self, *stringnumbers):
        sum = 0
        for string in stringnumbers:
            if string:
                if self.checkForNewLineSeparator(string) == -1:
                    return ''

                sum += float(string)
        return self.getStringResult(sum)

    def getStringResult(self, numberInFloatFormat):
        fractionalPartOfFloat = math.modf(numberInFloatFormat)[0]
        if fractionalPartOfFloat > 0:
            stringToReturn = str(numberInFloatFormat)
        else:
            stringToReturn = str(int(numberInFloatFormat))
        return stringToReturn

    def checkForNewLineSeparator(self, stringToCheck):
#        if stringToCheck.endswith('\n'):
#            return -1
        newLineIncorrectPosition = stringToCheck.find(',\n')
        if newLineIncorrectPosition > -1:
            sumOfSeparatedNumbers = 0.0
            listOfNumbers = stringToCheck.split('\n')
            for number in listOfNumbers:
                if number:
                    sum += float(number)
            return sumOfSeparatedNumbers
        else:
            #return wrong possition.

