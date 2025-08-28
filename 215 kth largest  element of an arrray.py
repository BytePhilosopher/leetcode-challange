# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 




import random

class Solution(object):
    def findKthLargest(self, nums, k):
        def quickselect(l, r, idx):
            pivot = nums[random.randint(l, r)]
            left, mid, right = [], [], []
            
            for n in nums[l:r+1]:
                if n < pivot:
                    left.append(n)
                elif n > pivot:
                    right.append(n)
                else:
                    mid.append(n)
            
            if idx < len(right):
                nums[l:r+1] = right + mid + left
                return quickselect(l, l+len(right)-1, idx)
            elif idx < len(right) + len(mid):
                return pivot
            else:
                nums[l:r+1] = right + mid + left
                return quickselect(r-len(left)+1, r, idx-len(right)-len(mid))
        
        # kth largest index in 0-based
        return quickselect(0, len(nums)-1, k-1)
    
