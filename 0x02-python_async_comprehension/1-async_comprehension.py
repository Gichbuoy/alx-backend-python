#!/usr/bin/env python3
"""
Async Comprehensions that takes no args, and collect 10 random no.
"""

import asyncio
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using an async comprehension
    over the async_generator coroutine.

    Returns:
    - List[int]: A list containing 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result  # type: ignore

if __name__ == '__main__':
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
