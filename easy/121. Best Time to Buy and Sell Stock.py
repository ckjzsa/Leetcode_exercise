class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        difference = [0 for _ in range(len(prices) - 1)]
        for i in range(len(prices) - 1):
            difference[i] = prices[i + 1] - prices[i]
        
        cummulated_profit = [0 for _ in range(len(prices) - 1)]
        cummulated_profit[0] = max(0, difference[0])
        maxProfit = cummulated_profit[0]

        for i in range(1, len(prices) - 1):
            cummulated_profit[i] = max(0, cummulated_profit[i - 1] + difference[i])
            maxProfit = max(maxProfit, cummulated_profit[i])
        
        return maxProfit
