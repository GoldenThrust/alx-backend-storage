#!/usr/bin/env python3
from datetime import datetime

get_page = __import__('web').get_page
if __name__ == "__main__":
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"

    start_time = datetime.now()
    result = get_page(slow_url)
    print(f"First call: {datetime.now() - start_time}")

    start_time = datetime.now()
    result = get_page(slow_url)
    print(f"Second call: {datetime.now() - start_time}")

    import time
    time.sleep(11)

    start_time = datetime.now()
    result = get_page(slow_url)
    print(f"Third call after cache expiration: {datetime.now() - start_time}")
