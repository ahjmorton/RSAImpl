def euclidean(num, mod) :
    mod = int(mod)
    num = int(num)
    while mod != 0 :
        tmp = mod
        mod = num % mod
        num = tmp
    return num

def extended_euclidean(lastd, d) :
    lastx= 0
    x = 1
    lastd = int(lastd)
    d = int(d)
    while d != 0:
        quo = int(lastd / d)
        tmpx = x
        tmpd = d
        x = lastx - quo * x
        d = lastd % d
        lastx = tmpx
        lastd = tmpd     
    return (d, lastd, x, lastx)
