# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        # convert all stones into negative (to simulate max heap)
        stones = [-s for s in stones]
        heapq.heapify(stones)  # build heap in O(n)

        while len(stones) > 1:
            # extract two heaviest (smallest negative numbers)
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                # push the remaining stone back
                heapq.heappush(stones, -(first - second))

        # return last stone or 0 if none
        return -stones[0] if stones else 0

# import heapq
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         nums = [-s for s in nums]   # negate all numbers to simulate max-heap
#         heapq.heapify(nums)         # turn nums into a heap

#         for i in range(k-1):
#             heapq.heappop(nums)
        

#         return  -nums[0]          # top of heap is kth largest

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # build a min-heap with first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        # for each remaining number, if it's bigger than the smallest in heap, replace it
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)  # pop+push in O(log k)
        return heap[0]
