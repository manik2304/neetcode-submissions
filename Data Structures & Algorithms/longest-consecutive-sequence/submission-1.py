class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set(nums)
        max_len = 0
        curr_len = 0

        for num in my_set:
            current_num = num
            while current_num in my_set:
                curr_len += 1
                current_num += 1
            max_len = max(max_len, curr_len)
            curr_len = 0

        return max_len


        