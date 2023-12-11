#!/usr/bin/env python3

"""
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - float: The average execution time per iteration.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n


if __name__ == '__main__':
    print("Execution time: {}".format(measure_time(5, 9)))
