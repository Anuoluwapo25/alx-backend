#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
use self.cache_data - dictionary from the parent class BaseCaching
discard the last item put in cache (LIFO algorithm)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache inherits from class BaseCaching
    """

    def __init__(self):
        """
        Initialize class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_item = self.keys.pop(0)
                del self.cache_data[discard_item]
                print('DISCARD: {}'.format(discard_item))

    def get(self, key):
        """
        Get an item by the key
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return (self.cache_data[key])
        return None
