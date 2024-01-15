#!/usr/bin/env python3
import asyncio
from typing import Union
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Union[int, float]]:
    """
    Function that creates an asyncio.Task for the wait_random coroutine.

    :param max_delay: Maximum delay in seconds.
    :type max_delay: int
    :return: asyncio.Task for wait_random.
    :rtype: asyncio.Task[Union[int, float]]
    """
    return asyncio.create_task(wait_random(max_delay))
