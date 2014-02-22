import math

def checkio(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return [0, 0, 0]
    ca = 0.5 * (b**2 + c**2 - a**2) / (b * c)
    cb = 0.5 * (c**2 + a**2 - b**2) / (c * a)
    cc = 0.5 * (a**2 + b**2 - c**2) / (a * b)
    l = map(lambda x: int(round(180 * math.acos(x) / math.pi)), (ca, cb, cc))
    return sorted(list(l))

if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60]
    assert checkio(3, 4, 5) == [37, 53, 90]
    assert checkio(2, 2, 5) == [0, 0, 0]
