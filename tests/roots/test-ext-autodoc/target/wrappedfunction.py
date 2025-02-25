from __future__ import annotations

from contextlib import contextmanager
from functools import lru_cache
from typing import Generator  # NoQA: TC003,UP035


@lru_cache(maxsize=None)  # NoQA: UP033
def slow_function(message, timeout):
    """This function is slow."""
    print(message)


@contextmanager
def feeling_good(x: int, y: int) -> Generator:
    """You'll feel better in this context!"""
    yield
