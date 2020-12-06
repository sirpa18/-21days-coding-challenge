# 414. Third Maximum Number

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:

# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = set(nums)
        num = sorted(nums)
        
        if len(num)<=2:
            return max(num)
        else:
            maxi = num[-3]
            return maxi
            
            
            
        