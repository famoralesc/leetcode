
def isHappy(n: int) -> bool:
    """
    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.

    Runtime 34 ms
    Beats 76.13% of users with Python3

    Memory 16.50 MB
    Beats 80.97% of users with Python3

    Examples
    -------
    >>> isHappy(n=19)
    True
    >>> isHappy(n=2)
    False
    """
    duplicate = {}
    total = 0
    while True:
        digits = []
        while n > 0:
            digit = n % 10
            digits.append(digit)
            n //= 10
        total = sum([d ** 2 for d in digits])
        if total == 1:
            return True
        n = total
        exits = duplicate.get(n, False)
        if exits:
            return False
        duplicate[total] = True
