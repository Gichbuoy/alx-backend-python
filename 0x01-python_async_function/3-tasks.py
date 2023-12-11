#!/usr/bin/env python3
"""
Create a task_wait_random function that takes an integer max_delay,
returns a `asyncio.Task`
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task for wait_random
    with the specified max_delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: A Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    async def test(max_delay: int):
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
