class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if len(s) == 0:
            return s

        s_rotate = s[:n]
        s = s[n:]

        return s + s_rotate
