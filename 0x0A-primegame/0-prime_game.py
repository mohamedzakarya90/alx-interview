#!/usr/bin/python3
""" The module for Prime Game """


def isWinner(x, nums):
    """
    determining  winner of  set of prime number removal 
    args->
        x (int)= number of rounds
        nums (list of int)= list of integers where each integer n is denotting
        set of consecutive integers which is starting from 1 up to&including n

    returns->
        str= name of player who won the most rounds either "Ben"
        or "Maria"
        none= if winner cannot be determined
    raises->
        none
    """
    # checking for an invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # initializing scores & array of possible prime numbers
    ben = 0
    maria = 0
    # creatting  list "a" of length sortd (nums)[-1] + 1 with all the elements
    # is been initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # first two elements of the list - a[0] and a[1] are been set to 0
    # because the 0 and the 1 are not prime numbers
    a[0], a[1] = 0, 0
    # Using sieve of eratosthenes algorithm for generatting an array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # playing each round of the game
    for i in nums:
        # if sum of the prime numbers in set is even - Ben wins
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # determining winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    removing multiples of prime number from array of possible prime
    numbers
    args->
        ls (list of int)= array of the possible prime numbers
        x (int)= prime number to remove multiples ofit
    returns->
        none
    raises->
        none
    """
    # that loop is iteratting over multiples of a prime number and marking them as
    # non-prime by setting their corresponding value to 0 in input
    # list ls it is Starting from 2 - it is setting every multiple of x up to the
    # length of ls to 0 and if the index i * x is out of range for list ls
    # the try block will raise exception which is IndexError  - the loop will
    # terminatting using break statement
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
