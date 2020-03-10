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

    
    
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x = str(x)
        p1 = 0
        p2 = -1

        while p1 <= (len(x) + p2):
            if x[p1] != x[p2]:
                return False
            
            p1 += 1
            p2 -= 1
        
        return True

