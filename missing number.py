# from Leetcode - 268
# Problem Statement:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space complexity
# and O(n) runtime complexity?

# Solution :

#find the total sum of n natural numbers.
#find the sum of given list
#subtract to find the missing value

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums_sum = sum(nums)

        cal_sum = n * (n + 1) // 2   #formula to find sum of n natural numbers

        return cal_sum - nums_sum

