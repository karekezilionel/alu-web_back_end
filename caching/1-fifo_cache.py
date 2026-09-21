#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache following FIFO algorithm

        Args:
            key: The key to add
            item: The value associated with the key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

        self.cache_data[key] = item
        self.order.append(key)

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
    