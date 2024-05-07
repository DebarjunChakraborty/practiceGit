def sieve_of_eratosthenes(n):
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

def main():
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    if lower_limit < 2:
        lower_limit = 2
    if upper_limit < 2:
        print("No prime numbers within the specified range.")
        return
    primes = sieve_of_eratosthenes(upper_limit)
    primes_in_range = [prime for prime in primes if prime >= lower_limit]
    if primes_in_range:
        print("Prime numbers between", lower_limit, "and", upper_limit, "are:", primes_in_range)
    else:
        print("No prime numbers within the specified range.")

if __name__ == "__main__":
    main()
