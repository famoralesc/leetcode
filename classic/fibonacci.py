import sys
import time

def fibonacci(number):
    """Calculate the fibonacci number using the traditional 
    recursive way.

    Examples
    --------
    >>> fibonacci(20)
    6765
    >>> fibonacci(11)
    89
    """
    if number < 2:
        return number
    return fibonacci(number -1 ) + fibonacci(number -2)

def fibonacci2(number):
    """Calculate the fibonacci number using dynamic programming.
    This solution stores the result on each iteration in a dictionary,
    such as 
    fib[number] = fib[number - 1] + fib[number - 2]ßß

    Examples
    --------
    >>> fibonacci2(20)
    6765
    >>> fibonacci2(11)
    89
    """
    fib = {}
    a, b = 0, 1
    if number < 2:
        return number
    n = 2
    while n <= number:
        fib[n] = fib.get(n - 1, a) + fib.get(n - 2, b)
        n += 1
    return fib[number]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the fibonacci number, ie : fibonacci.py 5")
        sys.exit(1)
    
    number = int(sys.argv[1])
    start = time.time()
    fib = fibonacci(number)
    elapsed = time.time() - start
    print("The fibonacci number for %s is %s in %1.10f seconds"%(number, fib, elapsed))
    
    start = time.time()
    fib = fibonacci2(number)
    elapsed = time.time() - start
    print("The fibonacci number for %s is %s in %1.10f seconds"%(number, fib, elapsed))

    