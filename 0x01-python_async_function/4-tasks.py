#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
task_wait_random is being called
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn task_wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - list: List of delays (float values) in ascending order.
    """
    delays = [task_wait_random(max_delay) for i in range(1, n + 1)]
    results = await asyncio.gather(*delays, return_exceptions=True)
    results = [
        result for result in results if not isinstance(result, Exception)
        ]
    return sorted(results)
