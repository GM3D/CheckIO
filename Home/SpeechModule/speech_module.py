FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def u20_text(l):
    if l < 10:
        return FIRST_TEN[l - 1]
    else:
        return SECOND_TEN[l - 10]

def u100_text(l):
    if l < 20:
        return u20_text(l)
    else:
        text = OTHER_TENS[l // 10 - 2]
        lowest_digit = l % 10
        lowest_text = ''
        if lowest_digit:
            lowest_text = FIRST_TEN[lowest_digit - 1]
        if text and lowest_text:
            return text + ' ' + lowest_text
        else:
            return text + lowest_text

def checkio(number):
    text = ''
    h = (number // 100)
    l = number % 100
    if h:
        text = FIRST_TEN[h - 1] + ' ' + HUNDRED
    if l:
        if text:
            text += ' ' + u100_text(l)
        else:
            text = u100_text(l)
    return text
    

if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    
