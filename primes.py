from math import sqrt

from prng import get_random

def sieve_of_atkins(limit):
    '''use sieve of atkins to find primes <= limit.'''
    primes = [0] * limit

    # n = 3x^2 + y^2 section
    xx3 = 3
    for dxx in xrange( 0, 12*int( sqrt( ( limit - 1 ) / 3 ) ), 24 ):
        xx3 += dxx
        y_limit = int(12*sqrt(limit - xx3) - 36)
        n = xx3 + 16
        for dn in xrange( -12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

        n = xx3 + 4
        for dn in xrange( 12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

    # n = 4x^2 + y^2 section
    xx4 = 0
    for dxx4 in xrange( 4, 8*int(sqrt((limit - 1 )/4)) + 4, 8 ):
        xx4 += dxx4
        n = xx4+1

        if xx4%3:
            for dn in xrange( 0, 4*int( sqrt( limit - xx4 ) ) - 3, 8 ):
                n += dn
                primes[n] = not primes[n]

        else:
            y_limit = 12 * int( sqrt( limit - xx4 ) ) - 36

            n = xx4 + 25
            for dn in xrange( -24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

            n = xx4+1
            for dn in xrange( 24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

    # n = 3x^2 - y^2 section
    xx = 1
    for x in xrange( 3, int( sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            s = 4

        for dn in xrange( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    xx = 0
    for x in xrange( 2, int( sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)-1
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            n -= 1
            s = 0

        for dn in xrange( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    # eliminate squares
    for n in xrange(5,int(sqrt(limit))+1,2):
        if primes[n]:
            for k in range(n*n, limit, n*n):
                primes[k] = False
    return [2,3] + filter(lambda x : primes[x], xrange(5, limit, 2))

def rabin_miller_pass(a, n) :
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def isprime(num, no_of_passes=20) :
    r = get_random()
    for repeat in xrange(no_of_passes):
        a = 0
        while a == 0:
            a = r.randrange(num)
        if not rabin_miller_pass(a, num):
            return False
    return True

def generate_prime_bits_simp(bit_length) :
    p = get_random().getrandbits(bit_length) | 1
    while not isprime(p) :
        p = get_random().getrandbits(bit_length) | 1
    return p

def generate_prime_bits(bit_length) :
    sieve = sieve_of_atkins(65000)
    testers = list()
    while len(testers) == 0 :
        testers = [get_random().getrandbits(bit_length) | 1 for x in xrange(1000)]
        for x in sieve :
            testers = filter(lambda y : y % x != 0, testers)
        testers = filter(isprime, testers)
        if len(testers) > 0 :
            return testers[0]

