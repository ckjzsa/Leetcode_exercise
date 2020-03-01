class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        delta = [0 for _ in range(len(prices) - 1)]
        for i in range(len(prices) - 1):
            delta[i] = prices[i+1] - prices[i]
        
        cummu_pro = [0 for _ in range(len(prices) - 1)]
        cummu_pro[0] = max(0, delta[0])
        for i in range(1, len(cummu_pro)):
            cummu_pro[i] = max(0, cummu_pro[i-1] + delta[i])

        return max(cummu_pro)
