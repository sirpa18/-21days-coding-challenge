#problem statement 169 - Majority element
# Given an array of size n, find the majority element. The majority element is the element 
#hat appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in 
#the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

		count = {}
    
        for i in nums:
            count[i] = count.get(i,0) +1
        
        for key,value in count.items():
            return max(count, key=count.get )


Logic:
1. HashMap is implemented to get the maximum count in a dictionary
2. The maximum value is returned from the stored dict named "count".
