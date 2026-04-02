class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0

        # left = 0
        # max_len = 0
        # win_dict = {}

        # for right, char in enumerate(s):
        #     win_dict[char] = win_dict.get(char, 0)  + 1
        #     while win_dict[char] > 1:
        #         current_char = s[left]
        #         win_dict[current_char] = win_dict[current_char]  - 1
        #         left += 1
        #     win_len = right-left+1
        #     max_len = max(max_len, win_len)
        # return max_len

        char_index = {} # store the indices
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index  and char_index[char] >= left:
                left = char_index[char]+1
            char_index[char] = right
            max_len = max(max_len, right-left+1)
        return max_len


        