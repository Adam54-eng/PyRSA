import math
import random

class RSAKey:

    @staticmethod
    def __is_prime(n):

        if n < 2: return False

        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0: return False

        return True

    def __init__(self, min_value, max_value):

        self.p = 6
        self.q = 6
        while not self.__is_prime(self.p):

            self.p = random.randint(min_value, max_value)

        while not self.__is_prime(self.q) or self.q == self.p:
        
            self.q = random.randint(min_value, max_value)

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

    def generate_encryption_key(self):

        e = random.randint(2, self.phi - 1)

        while math.gcd(e, self.phi) != 1:

            e = random.randint(2, self.phi - 1)

        self.e = e
        return e


    def generate_decryption_key(self):

        self.d = pow(self.e, -1, self.phi)
        return self.d

    def modular_pow(self, key, x):
        
        return pow(x, key, self.n)