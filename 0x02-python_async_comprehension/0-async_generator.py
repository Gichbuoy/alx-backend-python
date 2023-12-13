#!/usr/bin/env python3
"""
Async Generator that takes no args
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # typpe: ignore
    """
    Asynchronous generator coroutine that yields a random number
    between 0 and 10
    after asynchronously waiting for 1 second, repeated 10 times.

    Yields:
    - int: A random integer between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

    if __name__ == '__main__':
        async def print_yielded_values():
            result = []
            async for i in async_generator():
                result.append(i)
            print(result)

        asyncio.run(print_yielded_values())
