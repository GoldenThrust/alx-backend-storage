#!/usr/bin/env python3
import redis
import requests
from functools import wraps

rds = redis.Redis()


def cache_url(exp_time):
    """
    Decorator function for caching the result of a URL request in Redis.
    """
    def decorator(f):
        """ decorator function """
        wraps(f)

        def wrapper(url):
            """
            Wrapper function to check and retrieve the result from the
            cache or make a new request.
            """
            key = f"count:{url}"
            result = rds.get(key)

            if result:
                return result.decode('utf-8')

            res = f(url)

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
