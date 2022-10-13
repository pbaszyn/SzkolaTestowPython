class StringCalculator:
    def add(self, *stringnumbers):
        sum = 0
        for string in stringnumbers:
            if string:
                sum += int(string)
        return str(sum)
