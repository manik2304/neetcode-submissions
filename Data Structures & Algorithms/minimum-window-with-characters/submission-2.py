from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        have = 0   # no of chars (of t) meeting required freq
        need = Counter(t) # count the freq of chars of t
        win = defaultdict(int)
        need_count = len(need) # no of unique chars required
        min_len = float('inf')
        result = ""  # empty string

        for right, char in enumerate(s):
            win[char] += 1
            if char in need and win[char]==need[char]:
                have += 1
            while have == need_count:  # this window is valid
                win_len = right-left+1
                if win_len < min_len: # update the result if this is minimum
                    min_len = win_len
                    result = s[left:right+1]
                win[s[left]] -= 1
                if s[left] in need and win[s[left]]<need[s[left]]:
                    have -= 1
                left += 1

        return result

        