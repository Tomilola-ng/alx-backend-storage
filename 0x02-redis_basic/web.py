#!/usr/bin/env python3

""" WEB SCRAPY """

import requests
import redis
from functools import wraps
from time import time

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(expiration=10):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Create cache key
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"

            # Check if the page is cached
            cached_page = redis_client.get(cache_key)
            if cached_page:
                # Increment the access count
                redis_client.incr(count_key)
                return cached_page.decode('utf-8')

            # If not cached, call the original function
            page_content = func(url)

            # Cache the result
            redis_client.setex(cache_key, expiration, page_content)

            # Increment the access count
            redis_client.incr(count_key)

            return page_content
        return wrapper
    return decorator

@cache_page(expiration=10)
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
    
    # First request (will be slow)
    start_time = time()
    content = get_page(url)
    print(f"First request took {time() - start_time:.2f} seconds")
    
    # Second request (should be faster due to caching)
    start_time = time()
    content = get_page(url)
    print(f"Second request took {time() - start_time:.2f} seconds")
    
    # Print the access count
    count = redis_client.get(f"count:{url}")
    print(f"The URL was accessed {count.decode('utf-8')} times")
