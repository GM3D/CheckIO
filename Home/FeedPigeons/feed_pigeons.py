def pigeons(i):
    return i * (i + 1) / 2

def checkio(N):
    i = 1 # time
    remaining = N # remaining wheats
    feds = 0 # number of fed pigeons
    while remaining > 0:
        n = pigeons(i)
        feds_this_round = min(remaining, n)
        feds = max(feds, feds_this_round)
        remaining -= feds_this_round
        i += 1
    return feds

if __name__ == '__main__':
    for i in [5]:
        print "checkio(%d) = %d" % (i, checkio(i))
        
