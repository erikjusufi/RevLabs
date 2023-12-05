"""
Write a decorator that stores the result of a function call and returns the cached version in
subsequent calls (with the same parameters) for 5 minutes, or ten times whichever comes
first.
"""

import time

def parametrized_cache(timeout: int = 300, calls: int = 10) -> callable:
    def decorator(func: callable) -> callable:
        cache = {}

        def inner(*args, **kwargs):
            curr_time = time.time()
            if args in cache:
                if time.time() - cache[args]["time"] > timeout:
                    # TIMEOUT
                    # print("TIMEOUT")
                    cache[args] = {
                        "result": func(*args),
                        "time": curr_time,
                        "num_of_calls": 1,
                    }
                elif cache[args]["num_of_calls"] == calls:
                    # MAX NUMBER OF CALLS
                    # print("MAX NUMBER OF CALLS")
                    cache[args] = {
                        "result": func(*args),
                        "time": curr_time,
                        "num_of_calls": 1,
                    }
                else:
                    # RETURN CACHED RESULT
                    # print("CACHED")
                    cache[args]["num_of_calls"] += 1
            else:
                # INITIAL CALL AND CACHING
                # print("INITIAL CALL")
                cache[args] = {
                    "result": func(*args),
                    "time": curr_time,
                    "num_of_calls": 1,
                }
            return cache[args]["result"]

        return inner

    return decorator

@parametrized_cache(timeout=5, calls=3)
def multiply(a: [int, float], b: [int, float]) -> [int, float]:
    time.sleep(2)
    return a * b
