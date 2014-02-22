def checkio(word):
    lower = 0
    upper = 0
    number = 0
    if len(word) < 10:
        return False
    for c in word:
        if ord('a') <= ord(c) and ord (c) <= ord('z'):
            lower += 1
        elif ord('A') <= ord(c) and ord (c) <= ord('Z'):
            upper += 1
        elif ord('0') <= ord(c) and ord(c) <= ord('9'):
            number += 1
    if lower and upper and number:
        return True
    else:
        return False

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
