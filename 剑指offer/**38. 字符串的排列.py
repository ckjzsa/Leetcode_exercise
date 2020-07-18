class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        s = list(sorted(s))

        def helper(s, temp):
            if not s:
                res.append(''.join(temp))
            
            for i, char in enumerate(s):
                if i > 0 and s[i-1] == s[i]:
                    continue
                helper(s[:i]+s[i+1:], temp+[char])
        
        helper(s, [])
        return res
