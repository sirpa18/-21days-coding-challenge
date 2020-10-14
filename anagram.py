# from Leetcode - 242
# Problem Statement:


# Given two strings s and t , write a function to determine if t is an anagram of s.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_sort = sorted(s)
        t_sort = sorted(t)

        if s_sort == t_sort:
            return True
        else:
            return False
