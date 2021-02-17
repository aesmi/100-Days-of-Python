import functools
# Takes a parameter which represents maximum size of the cache
@functools.lru_cache(None)
def fib(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    return fib(n - 1) + fib(n - 2)