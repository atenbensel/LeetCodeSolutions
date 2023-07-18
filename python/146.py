class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) >= self.capacity:
            del_key = self.order.pop(0)
            del self.cache[del_key]

        self.cache[key] = value
        self.order.append(key)
