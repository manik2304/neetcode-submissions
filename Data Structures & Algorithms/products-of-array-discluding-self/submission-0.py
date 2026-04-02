class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_product = [1]*l
        right_product = 1
        product = [1]*l

        for i in range(1,l):
            left_product[i] = left_product[i-1]*nums[i-1]

        for j in range(l-1,-1,-1):
            product[j] = left_product[j]*right_product
            right_product *= nums[j]

        return product
        

        