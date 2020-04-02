class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.LRU = {}
        self.count = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.LRU[key]
            for i in self.count:
                if i != key:
                    self.count[i] -= 1
             
            self.count[key] = 0

            if len(self.LRU) > self.capacity:
                min_key = min(self.count, key=self.count.get)
                self.LRU.pop(min_key)
                self.count.pop(min_key)

            return value

        except Exception:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.LRU[key] = value
        self.count[key] = 0
        
        for i in self.count:
            if i != key:
                self.count[i] -= 1
            else:
                self.count[i] = 0


        if len(self.LRU) > self.capacity:
            min_key = min(self.count, key=self.count.get)
            self.LRU.pop(min_key)
            self.count.pop(min_key)
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
