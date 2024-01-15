#!/usr/bin/env python3
'''module 2'''

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay) and returns total_time / n.
    :param n: Number of times to spawn wait_random.
    :type n: int
    :param max_delay: Maximum delay in seconds.
    :type max_delay: int
    :return: Average time per wait_random call.
    :rtype: float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
