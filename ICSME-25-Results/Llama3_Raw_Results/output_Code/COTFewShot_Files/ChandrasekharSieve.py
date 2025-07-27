class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        sieve = [True] * (self.n + 1)
        sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers
        for current_prime in range(2, int(self.n ** 0.5) + 1):
            if sieve[current_prime]:
                for multiple in range(current_prime * current_prime, self.n + 1, current_prime):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def get_primes(self):
        return self.primes