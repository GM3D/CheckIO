def checkio(data):
    l = sorted(data)
    q, r = divmod(len(l), 2)
    return float(l[q - 1 + r] + l[q]) / 2.0

if __name__ == '__main__':
    print checkio([1, 2, 3, 4, 5])
    print checkio([3, 1, 2, 5, 3])
    print checkio([1, 300, 2, 200, 1])
    print checkio([3, 6, 20, 99, 10, 15])

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
