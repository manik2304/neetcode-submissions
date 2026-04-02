class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0]*n
        # dp[0] = 1
        # dp[1] = 2

        # if n<2: return dp[n-1]

        # for i in range(2,n):
        #     dp[i] = dp[i-1]+dp[i-2]

        # return dp[n-1]

        if n==1: return 1
        if n==2: return 2

        dp_1, dp_2 = 1,2

        for _ in range(2,n):
            dp = dp_1+dp_2
            dp_1 = dp_2
            dp_2 = dp
        
        return dp

    

        