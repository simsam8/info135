fib_cache = {1: 1, 2: 1}


def fib(n, use_cache):
    if use_cache and n in fib_cache:
        return fib_cache[n]
    elif n == 1 or n == 2:
        return 1
    else:
        fib_cache[n] = fib(n - 1, use_cache) + fib(n - 2, use_cache)
        return fib(n - 1, use_cache) + fib(n - 2, use_cache)


def display_fib(last_n, use_cache=True):
    """
    Without cache: O(2^N)
    With cache: O(N)
    """
    for n in range(1, last_n + 1):
        print(fib(n, use_cache))


display_fib(80, True)
