# cache_layer/decorators.py

import json
from django.core.cache import cache
from functools import wraps
from rest_framework.response import Response

def cache_decorator(ttl=300):
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
                print('showing cached response.!!!!!!')
                return Response(cached_response)

            # Call the original view function
            response = view_func(request, *args, **kwargs)

            # Cache the response based on its type
            if isinstance(response, Response):
                cached_data = response.data  # Get the data from the DRF Response
                cache.set(cache_key, cached_data, ttl)
            print('showing normal response.!!!!!!!!!!')
            return response
        
        return _wrapped_view
    return decorator
