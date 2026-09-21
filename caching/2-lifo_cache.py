#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize the LIFOCache
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item to the cache following LIFO algorithm

        Args:
            key: The key to add
            item: The value associated with the key
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD: {}".format(self.last_key))

        self.last_key = key

    def get(self, key):
        """ Retrieve an item from the cache

        Args:
            key: The key to retrieve

        Returns:
            The value associated with the key, or None if not found
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
    