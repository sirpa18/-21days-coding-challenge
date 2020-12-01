#189. Rotate Array
#Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i =0
        while (i<k):
            nums[:] = [nums[-1]] + nums[::1]
            nums.pop()
            i+=1
# logic:
#     - initiate the value i=0 and run the loop until k
#     - use slicing to shift the values