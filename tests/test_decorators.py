# tests/test_decorators.py

from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
from cache_layer.decorators import cache_decorator

# Sample view for testing
@cache_decorator(ttl=60)  # Cache for 1 minute
def mock_view(request):
    return "Hello, World!"

class CacheDecoratorTest(TestCase):
    
    def setUp(self):
        self.url = reverse('mock_view')  # Make sure to define a URL for this view

    def test_cache_decorator(self):
        response1 = self.client.get(self.url)
        self.assertEqual(response1.content, b"Hello, World!")  # Ensure correct response

        # Cache should store the response
        response2 = self.client.get(self.url)
        self.assertEqual(response2.content, b"Hello, World!")  # Same response
        self.assertEqual(response1.content, response2.content)  # Responses should match
