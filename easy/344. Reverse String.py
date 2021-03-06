class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = 1
        
        while(i < len(s) - j):
            s[i], s[-j] = s[-j], s[i]
            i += 1
            j += 1

        
        return s
