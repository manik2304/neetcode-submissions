class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # my_dict = {}

        # for num in nums:
            
        #     if my_dict.get(num,0)==1:
        #         return True
        #     my_dict[num] = my_dict.get(num,0)+1
            
        # return False
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
        