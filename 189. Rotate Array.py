# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if len(nums)!=1 and k<len(nums) and k!=0 and k>0:
        #     for R in range(k+1):
        #         # if (R+k)>=len(nums):
        #         #     tem=nums[R]
        #         #     nums[R]=nums[(R+k)-(len(nums)-1)]
        #         #     nums[(R+k)-(len(nums)-1)]=tem
        #         if R==k and len(nums)%2!=0:
        #             nums.append(nums[R])
        #             nums.remove(nums[R])
        #         elif R!=k :
        #             if len(nums)%2==0:
        #                 tem=nums[R]
        #                 nums[R]=nums[R+k]
        #                 nums[R+k]=tem
        #             elif len(nums)%2!=0:
        #                 tem=nums[R]
        #                 nums[R]=nums[R+k+1]
        #                 nums[R+k+1]=tem
        # elif (k>len(nums)):
        #         for L in range(len(nums)-1):
        #                 tem=nums[L]
        #                 nums[L]=nums[L+1]
        #                 nums[L+1]=tem
        # elif k==0:
        #     return

        # if len(nums)!=1 and k<len(nums):
        #     for R in range(k+1):
        #         for L in range(len(nums)-1):
        #             if len(nums)%2==0:
        #                 tem=nums[L]
        #                 nums[L]=nums[L+1]
        #                 nums[L+1]=tem
        #             else:
        #                 tem=nums[L]
        #                 nums[L]=nums[L+1]
        #                 nums[L+1]=tem
        # if k==0 and (len(nums)-k)==0:
        #     return
        # if len(nums)%2!=0:
        #     for r in range((len(nums)-k)):
        #         for l in range(len(nums)-1):
        #             tem=nums[l]
        #             nums[l]=nums[l+1]
        #             nums[l+1]=tem 
        # elif len(nums)%2==0:
        #      for r in range(k):
        #         for l in range(len(nums)-1):
        #             tem=nums[l]
        #             nums[l]=nums[l+1]
        #             nums[l+1]=tem                   


        n = len(nums)
        k = k % n  # To handle cases where k > len(nums)

 
        nums.reverse()
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the rest of the elements
        nums[k:] = reversed(nums[k:])

