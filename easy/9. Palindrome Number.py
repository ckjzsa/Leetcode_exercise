class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stack = []
        for num in str(x):
            stack.append(num)
        
        for i in range(len(stack)):
            if str(x)[i] != stack.pop():
                return False
        
        return True

