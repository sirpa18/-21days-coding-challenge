# 1089. Duplicate Zeros
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function.

# Example 1:

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # i/p : [1,0,2,3,0,4,5,0]
        # o/p : [1,0,0,2,3,0,0,4]
        # return null
        
        arr_len = len(arr)
        i = 0 
        while i < arr_len:
            
            if arr[i] == 0 and i+1 != arr_len:
                arr.insert(i+1,0)
                arr.pop()
                i += 2    
            else:
                i += 1
            
                
        
                
            
