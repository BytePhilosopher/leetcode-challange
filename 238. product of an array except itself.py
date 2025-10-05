# 238. Product of Array Except Self
# Solved
# Medium

# Topics
# premium lock icon
# Companies

# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if not nums:
        #     return []
        # answer = [0] * len(nums)
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             product*=nums[j]
        #         if j==(len(nums)-1):
        #                 answer[i]=product
        # return answer
        # if not nums:
        #     return []
        # answer = [0] * len(nums)
        
        # def pro(nums,n,k,answer):
        #     answer[k]=nums[k]
        #     for i in range(1,len(nums)):
        #         answer[i]=answer[i-1] * nums[i]
        #     if n>0 and k<(len(nums)):
        #         answer[k]=answer[n]
        #         n-=1
        #         k+=1
        #         pro(nums,n,k,answer)
        #     return
        # pro(nums,len(nums)-1,0,answer)
        # return answer

        n = len(nums)
        answer = [1] * n

        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        