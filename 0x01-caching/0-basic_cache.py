#!/usr/bin/python3
""" 0-main """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ inherited fron BaseCaching class """

    def put(self, key, item):
        """Add or update a key-value pair in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with a key from the cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
