class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        difference = []
        for i in range(len(prices) - 1):
            difference.append(prices[i+1] - prices[i])
        # cummulative = []
        cummulative = 0
        for i in difference:
            cummulative += max(0, i)
        
        return cummulative


