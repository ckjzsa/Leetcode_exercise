class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + " "
        stack, reverse = [], ""
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    reverse = reverse + stack.pop()
        
        return reverse[1:]
