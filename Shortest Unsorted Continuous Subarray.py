# 581. Shortest Unsorted Continuous Subarray
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:  
        if nums == sorted(nums) or len(nums) <=1:
            return 0
        nums_sorted = sorted(nums)
        if len(nums) == 2 and nums_sorted != nums:
            return len(nums)
        count = 0
        result = []
        zip_object = zip(nums, nums_sorted)
        for list1_i, list2_i in zip_object:
            result.append(list1_i-list2_i)
        index1 = result.index(next(filter(lambda x: x!=0, result)))
        for i in range(len(result)):
            if result[i] !=0:
                s = i
        index2 = s
        for i in range(index1,index2):
                count+=1
        return count+1
        