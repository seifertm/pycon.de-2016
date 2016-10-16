def fib(n):
    if n < 0:
        raise ValueError('Unable to compute negative Fibonacci values.')
    elif n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)
