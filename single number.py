# from Leetcode - 136
# Problem Statement:

#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# HASHMAP example.
# count the number of times a value is repeated and store it as a value in hashmap
# return the value which is equal to 1 .

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for key, value in count.items():
            if value == 1:
                return key








