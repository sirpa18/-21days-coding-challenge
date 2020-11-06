# 167. Two Sum II - Input array is sorted
# Given an array of integers that is already sorted in ascending order, find two numbers 
#such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to 
#the target, where index1 must be less than index2.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if (len(numbers)) == 1:
            return numbers
            
        complementMap = {}
        
        for i in range(len(numbers)):
            
            if numbers[i] in complementMap:                   
                return complementMap[numbers[i]]+1, i+1
            
            else:
                complementMap[target - numbers[i]] = i


# Logic:

1.	create a dict and find the complement of the iterable value[i]
2.	
        
        
        