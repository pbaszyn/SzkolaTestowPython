import math
import re

class StringCalculator:
    def add(self, *stringnumbers):
        floatSum = 0
        for string in stringnumbers:
            if string:
                floatSum = self.addStringToFloatSum(floatSum, string)
        return self.getStringResult(floatSum)

    def getStringResult(self, numberInFloatFormat):
        numberInFloatFormatAsString = "{:.15}".format(str(numberInFloatFormat))
        integerPartOfString = (re.search(r"^(\d+)", numberInFloatFormatAsString)).group()
        fractionPartOfString = ''
        if re.search("(\.\d*[1-9])", numberInFloatFormatAsString) != None:
            fractionPartOfString = (re.search("(\.\d*[1-9])", numberInFloatFormatAsString)).group()
        stringToReturn = integerPartOfString + fractionPartOfString
        return stringToReturn

    def addStringToFloatSum(self, floatSum, string):
        if self.ifStringWithSeparators(string):
            floatSum += self.sumListElements(self.getListOfStringNumbers(string))
        else:
            floatSum += float(string)
        return floatSum

    def sumListElements(self, list):
        elementsSum = 0
        for element in list:
            elementsSum += float(element)
        return elementsSum

    def ifStringWithSeparators(self, string):
        separatorsFound = False
        if string.find(',') != -1:
            separatorsFound = True
        return separatorsFound

    def getListOfStringNumbers(self, listAsString):
        return re.findall(r"(\d*\.\d*|[0-9]+)", listAsString)