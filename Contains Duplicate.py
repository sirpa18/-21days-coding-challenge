#from Leetcode - 217
# Problem Statement:
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

class Solution:
    #duplicate values cannot be added in a "set".
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_list = set(nums)
        if len(nums) == len(my_list):
            return False
        else:
            return True
