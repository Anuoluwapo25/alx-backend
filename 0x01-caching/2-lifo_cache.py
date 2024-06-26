#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
use self.cache_data - dictionary from the parent class BaseCaching
discard the last item put in cache (LIFO algorithm)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class FIFOCache inherits from class BaseCaching
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
                index = self.keys.index(key)
                item = self.keys.pop(index)
                self.keys.append(item)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_item = self.keys.pop(-2)
                del self.cache_data[discard_item]
                print('DISCARD: {}'.format(discard_item))

    def get(self, key):
        """
        Get an item by the key
        """
        if key and key in self.cache_data:
            return (self.cache_data.get(key))
        return None
