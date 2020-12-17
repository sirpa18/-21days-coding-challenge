# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char,0)+1
        for i in range(0,len(s)):
            if counts[s[i]] ==1 :
                return i
        return -1