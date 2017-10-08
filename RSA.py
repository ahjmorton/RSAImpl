from prng import get_random
from primes import generate_prime_bits
from euclid import extended_euclidean, euclidean


def rsa_primes(bit_length) :
    bit_length = int(bit_length) / 2
    p = generate_prime_bits(bit_length)
    q = generate_prime_bits(bit_length)
    while p == q :
        p = generate_prime_bits(bit_length)
        q = generate_prime_bits(bit_length)
    if p > q :
        return (p, q)
    else :
        return (q, p)

def generate_keys(bitlength) :
    r = get_random()
    p, q = rsa_primes(bitlength)
    n = p * q
    phin = (p - 1) * (q - 1)
    while True :
        e = r.randint(1, phin)
        while e == 1 or euclidean(e,  phin) != 1 :
            e = r.randint(1, phin)
        d = extended_euclidean(phin, e)[3]
        d = (d + phin) % phin
        return ((e, n),(d,n),(p,q))

def modexp(a, n, m):
	bits = []
	while n:
		bits.append(n%2)
		n /= 2
	solution = 1
	bits.reverse()
	for x in bits:
		solution = (solution*solution)%m
		if x:
			solution = (solution*a)%m
	return solution

def encrypt(message, key) :
    message = unicode(message)
    def mod_to_key(val) :
        return modexp(val, key[0], key[1])
    return map(mod_to_key, map(ord, message))

def decrypt(message, key) :
    def mod_to_key(val) :
        return modexp(val, key[0], key[1])
    return u"".join(map(unichr, map(mod_to_key, message)))

