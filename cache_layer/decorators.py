# cache_layer/decorators.py

import json
from django.core.cache import cache
from functools import wraps

def cache_decorator(ttl=300):
    """
    A caching decorator that caches the response of a view for a specified time.
    
    :param ttl: Time-to-live for cache in seconds (default is 300 seconds)
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Generate a unique cache key
            cache_key = f"{request.method}:{request.path}"
            if request.method == 'GET':
                cache_key += f":{json.dumps(request.GET)}"

            # Check if the response is cached
            cached_response = cache.get(cache_key)
            if cached_response:
                return cached_response

            # Call the original view function
            response = view_func(request, *args, **kwargs)

            # Store the response in the cache
            cache.set(cache_key, response, ttl)

            return response
        
        return _wrapped_view
    return decorator
