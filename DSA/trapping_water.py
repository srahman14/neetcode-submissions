class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        trapped = 0 

        while l < r:
            # get the max L, max R, and get the min
            if maxLeft < maxRight: 
                l+=1
                maxLeft = max(maxLeft, height[l])
                trapped += maxLeft - height[l] 
            else: 
                r-=1 
                maxRight = max(maxRight, height[r])
                trapped += maxRight - height[r]
        
        return trapped
