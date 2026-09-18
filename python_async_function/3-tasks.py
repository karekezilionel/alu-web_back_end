#!/usr/bin/env python3
"""Module that defines a task_wait_random function."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that runs wait_random with max_delay."""
    return asyncio.create_task(wait_random(max_delay))
