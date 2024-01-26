#!/usr/bin/env python3
import uuid
import redis
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments a counter in Redis for each function call.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ decorators wrapper """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores function inputs and outputs in Redis lists.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ decorators wrapper """
        in_key = "{}:inputs".format(method.__qualname__)
        out_key = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(in_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the inputs and outputs of a function stored in Redis.
    """
    in_key = "{}:inputs".format(method.__qualname__)
    out_key = "{}:outputs".format(method.__qualname__)
    print(in_key, out_key)
    inputs = method.__self__._redis.lrange(in_key, 0, -1)
    outputs = method.__self__._redis.lrange(out_key, 0, -1)
    print("{} was called {} times:".format(
        method.__qualname__, len(inputs)))
    for key, value in zip(outputs, inputs):
        value_str = value.decode("utf-8")
        key_str = key.decode("utf-8")
        print("{}(*{}) -> {}".format(method.__qualname__, value_str, key_str))


class Cache():
    """
    A class for caching and tracking function calls using Redis.
    """

    def __init__(self):
        """
        Initializes the Cache class with a Redis instance
        and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a unique key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Retrieves data from Redis using the provided key.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves an string from Redis using the provided key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves an integer from Redis using the provided key.
        """
        return self.get(key, fn=int)
