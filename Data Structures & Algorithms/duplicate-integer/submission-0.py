class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_dict = {}

        for num in nums:
            
            if my_dict.get(num,0)==1:
                return True
            my_dict[num] = my_dict.get(num,0)+1
            
        return False
        