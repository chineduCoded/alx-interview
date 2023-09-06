#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Find the overall winner"""
    max_limit = max(nums)
    prime_set = precompute_primes(max_limit)
    
    winners = [calculate_winner(n, prime_set) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def calculate_winner(n, prime_set):
    """Find round winner"""
    prime_count = sum(1 for p in prime_set if p <= n)
    return "Ben" if prime_count % 2 == 0 else "Maria"
        


def precompute_primes(limit):
    """Precompute primes"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    
    return set(primes)
