#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system with no limit """

    def put(self, key, item):
        """ Add an item to the cache

        Args:
            key: The key to add
            item: The value associated with the key
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

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
    