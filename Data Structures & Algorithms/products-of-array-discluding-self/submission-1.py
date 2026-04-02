class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_product = 1
        product = [1]*n

        for i in range(1,n):
            product[i] = product[i-1]*nums[i-1] # store the left product

        for j in range(n-1,-1,-1):
            product[j] *= right_product
            right_product *= nums[j]

        return product
        

        