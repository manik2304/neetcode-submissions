class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        max_freq = 0
        win_dict = {}

        for right, char in enumerate(s):
            win_dict[char]=win_dict.get(char,0)+1
            max_freq = max(max_freq, win_dict[char])
            win_len = right-left+1
            while win_len-max_freq>k:
                win_dict[s[left]] -= 1
                left += 1
                win_len -= 1
            max_len = max(max_len, win_len)

        return max_len

        