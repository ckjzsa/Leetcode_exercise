class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        if n == 0:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m+1)]

        res = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    dp[i][j] = 0
                elif matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    res = max(res, dp[i][j])
        
        return res ** 2
        
