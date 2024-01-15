#!/usr/bin/env python3
'''module 0'''
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds.

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
    return (delay)
