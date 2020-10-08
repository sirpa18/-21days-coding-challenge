# from Leetcode - 448
# Problem Statement:

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Solution :

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # set can be used to display the missing numbers.
        # 1. Iterate through the actual set of natural numbers
        # 2. subtract the actual set with the set that is given with missing numbers

        length = len(nums) + 1

        a = set([i for i in range(1, length)])  # actual set
        b = set(nums)  # missing number set
        return list(a - b)  # missing numbers

