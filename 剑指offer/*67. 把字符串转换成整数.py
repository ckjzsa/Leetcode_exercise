class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        
        res = 0
        sign = 1
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        boundary = 2 ** 31 // 10
        
        i = 1
        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            i = 0

        for s in str[i:]:
            if not '0' <= s <= '9':
                break
            if res > boundary or (res == boundary and s > '7'):
                return int_max if sign == 1 else int_min
            
            res = res * 10 + ord(s) - ord('0')
        
        return res * sign

