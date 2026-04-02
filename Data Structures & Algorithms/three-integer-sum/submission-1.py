class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array, O(n log n)

        n = len(nums)
        my_list = []

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue # skips duplicate i
            left = i+1
            right = n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    my_list.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return my_list



