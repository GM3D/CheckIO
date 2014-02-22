def checkio(n):
    text = ''
    q, n = divmod(n, 1000)
    if q:
        text += 'M' * q
    q, r = divmod(n, 100)
    if q == 4:
        text += 'CD'
    elif q == 9:
        text += 'CM'
    else:
        q1, r1 = divmod(n, 500)
        if q1:
            text += 'D'
        text += 'C' * (r1 // 100)
    q = r // 10
    if q == 4:
        text += 'XL'
    elif q == 9:
        text += 'XC'
    else:
        q1, r1 = divmod(r, 50)
        if q1:
            text += 'L'
        text += 'X' * (r1 // 10)
    r = r % 10
    if r == 4:
        text += 'IV'
    elif r == 9:
        text += 'IX'
    else:
        q1, r1 = divmod(r, 5)
        if q1:
            text += 'V'
        text += 'I' * r1
    return text
            
if __name__ == '__main__':
    assert checkio(6) == 'VI'
    assert checkio(76) == 'LXXVI'
    assert checkio(1954) == 'MCMLIV'
    assert checkio(1990) == 'MCMXC'
    assert checkio(2014) == 'MMXIV'
    for i in (6, 76, 1954, 1990, 2014):
        print(checkio(i))
