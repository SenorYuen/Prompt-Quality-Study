class ChandrasekharSieve:
    def __init__(self, n):
        # Initialize the limit and a boolean array, prime, of size n+1
        self.n = n
        self.prime = [True] * (n + 1)
        # 0 and 1 are not prime numbers
        self.prime[0] = self.prime[1] = False

    def generate_primes(self):
        # Iterate from 2 to sqrt(n)
        for p in range(2, int(self.n ** 0.5) + 1):
            # If p is a prime, mark as composite all the multiples of p
            if self.prime[p]:
                # Start from p*p because all the multiples of p less than p*p have already been marked
                for i in range(p * p, self.n + 1, p):
                    self.prime[i] = False

    def get_primes(self):
        # Return a list of all prime numbers in the range [2, n]
        return [p for p in range(2, self.n + 1) if self.prime[p]]

# Example usage
if __name__ == "__main__":
    sieve = ChandrasekharSieve(30)
    sieve.generate_primes()
    print(sieve.get_primes())