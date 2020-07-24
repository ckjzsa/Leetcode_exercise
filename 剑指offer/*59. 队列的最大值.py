class MaxQueue(object):

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def max_value(self):
        """
        :rtype: int
        """
        if len(self.max_queue) == 0:
            return -1
        else:
            return self.max_queue[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)
            
    def pop_front(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            return -1
        value = self.queue.pop(0)
        if value == self.max_queue[0]:
            self.max_queue.pop(0)
        
        return value


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
