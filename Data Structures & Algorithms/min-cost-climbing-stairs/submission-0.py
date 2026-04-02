class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0]*n # this holds the minimum cost to reach stairs

        # if n<2:
        #     return cost[n-1]
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2,n):
        #     dp[i] = cost[i]+min(dp[i-1], dp[i-2])

        # return min(dp[n-1], dp[n-2])

        n = len(cost)
        if n<2:
            return cost[n-1]

        long_prev, prev = cost[0], cost[1]

        for i in range(2,n):
            min_cost = cost[i]+min(long_prev, prev)
            long_prev = prev
            prev = min_cost

        return min(long_prev, prev)


        