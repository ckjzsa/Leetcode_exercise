class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(m, n):
            while m % n:
                m, n = n, m % n
            
            return n
        
        if len(deck) == 0 or len(deck) == 1:
            return False

        res_dict = {}
        for i in set(deck):
            res_dict[i] = 0

        for i in deck:
            res_dict[i] += 1
        
        g = res_dict.values()[0]
        for i in range(1, len(res_dict.values())):
            g = gcd(res_dict.values()[i], g)

        return g >= 2
    
       
