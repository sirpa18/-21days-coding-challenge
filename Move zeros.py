# problem statement- 283: 
# Given an array nums, write a function to move all 0's to the end of it while maintaining 
#the relative order of the non-zero elements.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """

        pos = 0
    
        for i in range(len(nums)):
            element = nums[i]
                
            if element != 0:
                nums[pos],nums[i] = nums[i], nums[pos]
                pos +=1

# Logic:

# 1. move the position of the element if its not zero to the first index in the list
                    
    
                
        