class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set(nums)
        max_len = 0
        curr_len = 0

        for num in my_set:
            if num-1 not in my_set:
                curr_num = num
                curr_len = 1
                while curr_num+1 in my_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)

        return max_len


        