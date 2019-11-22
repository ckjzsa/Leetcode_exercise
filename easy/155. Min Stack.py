class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        if len(self.minimum) == 0 or x < self.minimum[-1]:
            self.minimum.append(x)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) >= 1:
            self.minimum.pop()
            return self.stack.pop()
        else: 
            return 'error'
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) >= 1:
            pop_num = self.stack[-1]
            return pop_num
        else: 
            return 'error'

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) >= 1:
            return self.minimum[-1]
        else: 
            return 'error'

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
