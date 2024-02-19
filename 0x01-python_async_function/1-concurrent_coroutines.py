#!/usr/bin/env python3
"""
Async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay.
You will spawn wait_random n times with the specified max_delay.
Wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.
"""


import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays
