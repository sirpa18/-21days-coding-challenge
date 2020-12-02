# Given an array nums of n integers, are there elements a, b, c in nums such 
#that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sort1 = sorted(nums)
        for i in range(0,len(sort1)-2):
            left = i+1
            right = len(sort1)-1
            while left < right:
                target = sort1[i]+sort1[left]+sort1[right]
                if target == 0:
                    result.add((sort1[i],sort1[left],sort1[right]))
                    left+=1
                    right-=1
                elif target < 0:
                    left+=1
                else:
                    right-=1
        return result
                    
        
        