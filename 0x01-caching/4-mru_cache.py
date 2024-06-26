#!/usr/bin/python3
"""
MRU algorithm
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that uses the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """
        Initializes the MRUCache object.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Adds a new key-value pair to the cache.

        Args:
            key (str): The key to add to the cache.
            item (str): The value to associate with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Retrieves the value associated with a given key from the cache.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            str: The value associated with the key, or None if the key is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
         
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
