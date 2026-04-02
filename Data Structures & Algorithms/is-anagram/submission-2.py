class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

    #   if len(s) != len(t):
    #     return False

    #   my_dict = {}

    #   for char in s:
    #     my_dict[char] = my_dict.get(char,0)+1

    #   for char in t:
    #     my_dict[char] = my_dict.get(char,0)-1
    #     if my_dict[char] < 0:
    #         return False
    #   return True

    ## O(1) space complexity for only lower case letters

    
        if len(s) != len(t):
            return False

        my_list = [0]*26

        for char in s:
            my_list[ord(char)-ord('a')] += 1

        for char in t:
            index = ord(char) - ord('a')
            my_list[index] -= 1
            if my_list[index] < 0:
                return False
        return True




    