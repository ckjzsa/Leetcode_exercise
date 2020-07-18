class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        if len(num) == 1:
            return 1

        dp = [0] * len(num)
        dp[0] = 1
        dp[1] = 1 if int(num[:2]) > 25 else 2

        for i in range(2, len(num)):
            if int(num[i-1:i+1]) < 26 and int(num[i-1]) != 0:           
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[-1]
