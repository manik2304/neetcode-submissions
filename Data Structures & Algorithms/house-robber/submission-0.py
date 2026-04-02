class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0: return 0
        if n == 1: return nums[0]

        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2,n):
            max_rob = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = max_rob

        return prev1
        