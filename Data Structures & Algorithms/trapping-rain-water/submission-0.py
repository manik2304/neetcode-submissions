class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        maxL = [0]*n
        maxR = [0]*n
        maxW = 0

        for i in range(1,n):
            maxL[i] = max(maxL[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i+1], height[i+1])

        for i in range(n):
            maxW += max(min(maxL[i],maxR[i])-height[i],0)

        return maxW
            


        