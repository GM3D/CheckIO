def checkio(s):
    s = s.lower()
    hist = [s.count(chr(c)) for c in xrange(ord('a'), ord('z'))]
    max_count = 0
    max_char = 'a'
    for i in xrange(len(hist)):
        if hist[i] > max_count:
            max_count = hist[i]
            max_char = chr(ord('a') + i)
    return max_char

if __name__ == '__main__':
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
        
