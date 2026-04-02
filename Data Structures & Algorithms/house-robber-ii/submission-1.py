class Solution:
    def rob(self, nums: List[int]) -> int:

        def sub_rob(start, end):
            prev2, prev1 = 0, 0

            for i in range(start, end):
                max_rob = max(nums[i]+prev2, prev1)
                prev2 = prev1
                prev1 = max_rob

            return prev1

        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        return max(sub_rob(0,n-1), sub_rob(1,n))




        