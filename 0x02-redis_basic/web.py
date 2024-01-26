#!/usr/bin/env python3
""" Site Cache """
import redis
import requests
from functools import wraps
from typing import Callable

rds = redis.Redis()


def cache_url(exp_time: int) -> Callable[[Callable], Callable]:
    """
    Decorator function for caching the result of a URL request in Redis.
    """
    def decorator(method: Callable) -> Callable:
        """ decorator function """

        @wraps(method)
        def wrapper(url: str) -> str:
            """
            Wrapper function to check and retrieve the result from the
            cache or make a new request.
            """
            count = "count:{}".format(url)
            key = "result:{}".format('url')

            rds.incr(count)

            result = rds.get(key)

            if result:
                return result.decode('utf-8')

            res = method(url)
            rds.set(count, 0)
            rds.setex(key, exp_time, res)

            return res

        return wrapper

    return decorator


@cache_url(10)
def get_page(url: str) -> str:
    """
    Retrieve the content of a web page and cache the result.
    """
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.text
    else:
        return "Unable to access {}. Status code: {}".format(
                url, resp.status_code)
