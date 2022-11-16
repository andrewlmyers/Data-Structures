def factorial(n, cache={}):

    if n == 0:
        return 1
    if n not in cache:
        cache[n] = n * factorial(n-1, cache)
    return cache[n]
print(factorial(7))