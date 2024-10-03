#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes"""
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:  # Changed this line
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:
            prime_numbers.append(p)
    return prime_numbers


def count_prime_moves(n, primes):
    """Count the number of valid moves in a game with n numbers"""
    numbers = [True] * (n + 1)  # Represents available numbers
    moves = 0
    for prime in primes:
        if prime > n:
            break
        if numbers[prime]:
            # Make a move by removing prime and its multiples
            for multiple in range(prime, n + 1, prime):
                numbers[multiple] = False
            moves += 1
    return moves


def isWinner(x, nums):
    """Determine the winner after x rounds of the game"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n, primes)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

