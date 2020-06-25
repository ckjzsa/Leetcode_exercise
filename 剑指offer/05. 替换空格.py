class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        res = ''
        for i in s:
            if i != ' ':
                res += i
            else:
                res += '%20'

        return res
