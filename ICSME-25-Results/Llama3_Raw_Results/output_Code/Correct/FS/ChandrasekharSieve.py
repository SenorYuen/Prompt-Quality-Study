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

    # Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm
    def generate_primes(self):
        # Create a boolean array, prime, of size n+1
        prime = [True] * (self.n + 1)
        prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

        # Iterate from 2 to sqrt(n)
        for p in range(2, int(self.n ** 0.5) + 1):
            # If p is a prime, mark as composite all the multiples of p
            if prime[p]:
                for i in range(p * p, self.n + 1, p):
                    prime[i] = False

        # Return a list of all prime numbers in the range
        return [p for p in range(2, self.n + 1) if prime[p]]

    # Get the list of generated prime numbers
    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes