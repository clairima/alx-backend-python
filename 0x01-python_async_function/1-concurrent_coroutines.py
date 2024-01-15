#!/usr/bin/env python3
'''module 1'''
import asyncio
import random
from typing import List


async def wait_random(max_delay=10) -> float:
    """
    Asynchronous coroutine that waits
    for a random delay between 0 and max_delay seconds.

    :param max_delay: Maximum delay in seconds (default is 10).
    :type max_delay: float
    :return: Random delay that was waited.
    :rtype: float
    """
    # Generate a random delay between 0 and max_delay (inclusive) seconds
    delay = random.uniform(0, max_delay)

    # Asynchronously sleep for the calculated delay
    await asyncio.sleep(delay)

    # Return the random delay
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns
    wait_random n times with the specified max_delay.

    :param n: Number of times to spawn wait_random.
    :type n: int
    :param max_delay: Maximum delay in seconds.
    :type max_delay: int
    :return: List of delays in ascending order.
    :rtype: List[float]
    """
    # Use asyncio.gather to concurrently execute wait_random n times
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Return the list of delays in ascending order
    return sorted(delays)
