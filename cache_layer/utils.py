# cache_layer/utils.py

def generate_cache_key(request):
    """
    Generate a unique cache key based on the request method and path.
    Optionally include query parameters for GET requests.

    :param request: The Django request object
    :return: A unique cache key string
    """
    cache_key = f"{request.method}:{request.path}"
    if request.method == 'GET':
        cache_key += f":{request.GET.urlencode()}"
    return cache_key
