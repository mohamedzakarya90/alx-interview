#!/usr/bin/python3
""" the module is defining isWinner function"""


def isWinner(x, nums):
    """ this function for getting the one who won in the prime game """
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"

    return None


def is_prime(n):
    """ returning the True if n is prime and else the False"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """ returning list of the prime numbers between start and end which is  inclusive"""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
