class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        if self.n < 2:
            return []
        
        prime = [True] * (self.n + 1)
        p = 2
        while p * p <= self.n:
            if prime[p]:
                for i in range(p * p, self.n + 1, p):
                    prime[i] = False
            p += 1
        
        return [p for p in range(2, self.n + 1) if prime[p]]

    def get_primes(self):
        return self.primes