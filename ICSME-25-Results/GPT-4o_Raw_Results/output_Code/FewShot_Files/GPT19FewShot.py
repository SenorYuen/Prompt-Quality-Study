class ChandrasekharSieve:
    """
    This is a class that uses the Chandrasekhar's Sieve method to find all prime numbers within the range
    """

    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        :param n: int, the upper limit for generating prime numbers
        """
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.generate_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
        # Initialize a boolean array that marks whether each number is prime
        is_prime = [True] * (self.n + 1)
        p = 2
        
        # Iterate over each number starting from 2
        while (p * p <= self.n):
            # If is_prime[p] is not changed, then it is a prime
            if is_prime[p]:
                # Mark all multiples of p as not prime
                for i in range(p * p, self.n + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Collect all prime numbers
        prime_numbers = [p for p in range(2, self.n + 1) if is_prime[p]]
        return prime_numbers

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        >>> cs = ChandrasekharSieve(20)
        >>> cs.get_primes()
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
        return self.primes