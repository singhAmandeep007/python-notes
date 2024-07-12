"""
This script demonstrates the use of decorators to cache the results of a function
and count the number of times a function is called.
"""

import functools
import time


def count_calls(func):
    """
    This function is a decorator that keeps track of the number of times a function is called.
    It takes a function as input
    and returns a new function that behaves exactly like the input function,
    but also increments a counter and prints the number of calls each time the function is called.

    :param func: The function to be decorated.
    :return: The decorated function that counts and prints the number of calls.
    """

    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1  # track no. of calls
        # !r is for __repr__ representation
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = {}
    return wrapper_cache


@count_calls
def fibonacci_v1(num):
    if num < 2:
        return num
    return fibonacci_v1(num - 1) + fibonacci_v1(num - 2)


@cache
@count_calls
def fibonacci_v2(num):
    if num < 2:
        return num
    return fibonacci_v2(num - 1) + fibonacci_v2(num - 2)


@timer
def timed_fibonacci_v1(num):
    result = fibonacci_v1(num)
    print(result)


@timer
def timed_fibonacci_v2(num):
    result = fibonacci_v2(num)
    print(result)


print("timed_fibonacci_v1(15) \n")
timed_fibonacci_v1(15)
print("\n timed_fibonacci_v2(15) \n")
timed_fibonacci_v2(15)
