# 154. Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you 
#beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.



class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        nums_min = min(nums)
        
        for i in nums:
            for j in range(1,len(nums)):
                if i == j and nums_min == i:
                    return i
                else:
                    return nums_min


# logic:

# 1.    check if the duplicates can affect the minimum value obtained
# 2.    if duplicates exist, return one value.
                    