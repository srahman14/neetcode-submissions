# 217 Cotnains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array
# and return false if every element is disticnt

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool: 
        seen = set() 
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i) 
        
        return False

sol = Solution() 
arr = [1,2,2,3,4,5]
print(sol.hasDuplicate(arr))
