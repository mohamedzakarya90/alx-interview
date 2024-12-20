#!/usr/bin/python3
""" minimum operations
    """


def minOperations(n: int) -> int:
    """ minimum operations which are needed to get the n H characters """
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
