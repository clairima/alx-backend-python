#!/usr/bin/env python3
'''module 4'''

import asyncio
from typing import List, Union
from 3-tasks import task_wait_random
from 1-concurrent_coroutines import wait_n


def task_wait_n(n: int,
                max_delay: int) -> asyncio.Task[List[Union[int, float]]]:
    """
    Function that creates an asyncio.Task for the wait_n coroutine.

    :param n: Number of times to spawn task_wait_random.
    :type n: int
    :param max_delay: Maximum delay in seconds.
    :type max_delay: int
    :return: asyncio.Task for wait_n.
    :rtype: asyncio.Task[List[Union[int, float]]]
    """
    return asyncio.create_task(wait_n(n, max_delay))
