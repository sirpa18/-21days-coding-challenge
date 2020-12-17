# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        summ = 0
        count = 0
        mapp = {0:1}
        
        for i in range(len(nums)):
            summ += nums[i]
            
            if (summ -k) in mapp:
                count += mapp.get(summ-k)
            mapp[summ] = mapp.get(summ,0)+1
        
        return count