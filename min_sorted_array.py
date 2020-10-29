# problem statement:
# 153. Find Minimum in Rotated Sorted Array:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to 
# you beforehand. (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Return the minimum element of this array.



class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if (len(nums) == 1):
            return nums[0]
        
        nums_min = min(nums)
        
        return nums_min

#logic:

#the array is said to be rotated at anypoint of pivot . so its necessary to take the minimum value
#at the beginnig of the iteration.

