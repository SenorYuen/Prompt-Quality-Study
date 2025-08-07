'''
# This is a class that uses the Chandrasekhar's Sieve method to find all prime numbers within the range

class ChandrasekharSieve:
    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        """

    def generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        """

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """

'''


class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        if self.n < 2:
            return []

        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False

        p = 2
        while p * p <= self.n:
            if sieve[p]:
                for i in range(p * p, self.n + 1, p):
                    sieve[i] = False
            p += 1

        primes = []
        for i in range(2, self.n + 1):
            if sieve[i]:
                primes.append(i)

        return primes

    def get_primes(self):
        return self.primes


