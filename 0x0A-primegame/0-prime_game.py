#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to 'n' using the Sieve of Eratosthenes algorithm.

    Args:
    n (int): The upper limit for prime number generation.

    Returns:
    list: A list of prime numbers up to 'n'.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]

def calculate_winner(n):
    """
    Determine the winner of a game round based on the count of prime numbers in the range from 2 to 'n'.

    Args:
    n (int): The value of 'n' for the game round.

    Returns:
    str: The name of the winner ('Maria' or 'Ben').
    """
    primes = sieve_of_eratosthenes(n)
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"

def isWinner(x, nums):
    """
    Determine the winner of multiple game rounds.

    Args:
    x (int): The number of rounds to play.
    nums (list): A list of 'n' values for each game round.

    Returns:
    str or None: The name of the overall winner ('Maria' or 'Ben') or None if the winner cannot be determined.
    """
    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
