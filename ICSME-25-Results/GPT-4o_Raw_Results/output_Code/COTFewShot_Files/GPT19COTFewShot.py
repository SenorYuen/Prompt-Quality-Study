class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        if self.n < 2:
            return []
        is_prime = [True] * (self.n + 1)
        p = 2
        while p * p <= self.n:
            if is_prime[p]:
                for i in range(p * p, self.n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, self.n + 1) if is_prime[p]]

    def get_primes(self):
        return self.primes