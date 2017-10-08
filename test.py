import unittest

import prng
import RSA
import primes
import euclid

class RSAImplementationTest(unittest.TestCase) :

    def test_getting_rsa_primes(self) :
        pass

    def test_generating_keys(self) :
        pass

    def test_encryption(self) :
        pass

    def test_decryption(self) :
        pass

    def test_encryption_decryption_symmetrical(self) :
        pass

class PrimeModuleTest(unittest.TestCase) :

    def test_is_prime(self) :
        self.assertTrue(primes.isprime(11))
        self.assertTrue(not primes.isprime(10))

    def test_generating_prime_bits(self) :
        pass

class RandomModuleTest(unittest.TestCase) :

    def test_getting_random_is_same_object(self) :
        rand1 = prng.get_random()
        rand2 = prng.get_random()
        self.assertTrue(rand1 is rand2)

class EuclideanModuleTest(unittest.TestCase) :

    def test_euclidean(self) :
        res1 = euclid.euclidean(2, 11)
        self.assertTrue(res1 == 1)
        res2 = euclid.euclidean(4, 6)
        self.assertTrue(res2 == 2)

    def test_extended_euclidean(self) :
        pass

if __name__ == "__main__" :
    unittest.main()
