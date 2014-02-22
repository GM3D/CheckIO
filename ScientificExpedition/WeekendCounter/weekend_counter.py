from datetime import date, timedelta

def checkio0(start, end):
    count = 0
    d = start
    while d <= end:
        if d.weekday() == 5 or d.weekday() == 6:
            count += 1
        d += timedelta(days=1)
    return count

def checkio(start, end):
    q, r = divmod((end - start).days, 7)
    d1 = start.weekday()
    d2 = (d1 + r) % 7
    if d2 < d1:
        d2 += 7
    return q * 2 + (d1 <= 5 and 5 <= d2) + (d1 <= 6 and 6 <= d2)

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2
