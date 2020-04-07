class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_count = [0] * 26
        s_count = [0] * 26

        for i in p:
            p_count[ord(i) - 97] += 1
        
        left = 0
        
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue

            s_count[ord(s[right]) - 97] += 1

            if s_count == p_count:
                res.append(left)

            s_count[ord(s[left]) - 97] -= 1
            left += 1

        return res


        
                
