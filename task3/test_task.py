import unittest
import time
from task import parametrized_cache, multiply

class TestParametrizedCacheDecorator(unittest.TestCase):

    def test_cache_timeout(self):
        # Apply the decorator to the function with shorter timeout and call count for testing
        self.cached_multiply = parametrized_cache(timeout=5, calls=3)(multiply)
        initial_time = time.time()  # Get the current time

        result_1 = self.cached_multiply(2, 3)  # First call - should compute result, 2 seconds
        result_2 = self.cached_multiply(2, 3)  # Second call - should return cached result, 0 seconds
        time.sleep(3)  # Simulate time passage more than the timeout, 1 second
        result_3 = self.cached_multiply(2, 3)  # Third call - should recompute result as cache expired, 2 seconds
        self.assertGreaterEqual(time.time() - initial_time, 7)  # Check if the time needed for the test is at least 5 seconds

if __name__ == '__main__':
    unittest.main()
