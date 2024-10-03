#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return sieve

def calculate_winner(nums, prime_sieve):
    """Determine the winner for each game"""
    max_n = len(prime_sieve) - 1
    # Precompute the number of prime selections up to n
    prime_moves = [0] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        prime_moves[i] = prime_moves[i - 1]
        if prime_sieve[i]:
            # Prime number found, increase the count of moves
            for multiple in range(i, max_n + 1, i):
                prime_moves[multiple] += 1

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def isWinner(x, nums):
    """Determine the overall winner of the game"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_sieve = sieve_of_eratosthenes(max_n)
    
    return calculate_winner(nums, prime_sieve)
