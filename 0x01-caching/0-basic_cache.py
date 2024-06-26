#!/usr/bin/python3
"""caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    inherited fron BaseCaching class 
    """

    def put(self, key, item):
        """
        Add or update a key-value pair in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.
        """
        if key and key in self.cache_data:
            return (self.cache_data.get(key))
        return None
