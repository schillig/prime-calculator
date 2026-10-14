def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    first_100_primes = get_primes(100)
    print(f"The first 100 prime numbers are:\n{first_100_primes}")