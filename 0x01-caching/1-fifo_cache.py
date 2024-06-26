#!/usr/bin/python3
"""caching system """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherited from BaseCaching
    """
    def __init__(self):
        """
        init class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        put an item in cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) >= BaseCaching.MAX_ITEMS:
                del_item = self.keys.pop(0)
                del self.cache_data[del_item]
                print('DISCARD: {}'.format(del_item))

    def get(self, key):
        """
        get
        """
        if key and key in self.cache_data:
            return (self.cache_data.get(key))
        return None
