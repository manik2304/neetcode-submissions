class Solution:
    def findPivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] <= nums[-1]:
                pivot_index = mid
                right = mid-1
            else:
                left = mid+1
        return pivot_index

    def search(self, nums: List[int], target: int) -> int:
        pivot_ind = self.findPivot(nums)

        if pivot_ind == 0:
            left, right = 0, len(nums)-1
        elif target>= nums[0] and target<= nums[pivot_ind-1]:
            left, right = 0, pivot_ind-1
        else:
            left, right = pivot_ind, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left= mid+1
            
        return -1

        

        
    