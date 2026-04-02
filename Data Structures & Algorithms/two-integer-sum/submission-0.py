class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for ind, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target-num], ind]
            my_dict[num]=ind