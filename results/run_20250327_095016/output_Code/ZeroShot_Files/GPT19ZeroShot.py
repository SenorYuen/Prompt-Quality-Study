class ChandrasekharSieve:
    def __init__(self, n):
        """
        Initialize the ChandrasekharSieve class with the given limit.
        :param n: int, the upper limit to find prime numbers
        """
        self.n = n  # Store the upper limit
        self.primes = []  # Initialize an empty list to store prime numbers

    def generate_primes(self):
        """
        Generate prime numbers up to the specified limit using the Chandrasekhar sieve algorithm.
        :return: list, a list of prime numbers
        """
        if self.n < 2:
            self.primes = []  # No primes less than 2
            return self.primes

        # Initialize a list to track prime status of numbers
        is_prime = [True] * (self.n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Implementing the sieve
        for start in range(2, int(self.n**0.5) + 1):
            if is_prime[start]:
                # Mark all multiples of start as non-prime
                for multiple in range(start * start, self.n + 1, start):
                    is_prime[multiple] = False

        # Collecting all prime numbers
        self.primes = [num for num, prime in enumerate(is_prime) if prime]
        return self.primes

    def get_primes(self):
        """
        Get the list of generated prime numbers.
        :return: list, a list of prime numbers
        """
        return self.primes