# 121. Best Time to Buy and Sell Stock
# Solved
# Easy

# Topics
# premium lock icon
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if (prices[j]-prices[i])>profit:
        #             profit=prices[j]-prices[i]
        # return profit

        # def best_profit(s,profit,prices):
        #     for b in range(s):
        #         if profit<(prices[s]-prices[b]):
        #             profit=prices[s]-prices[b]
        #     s=s-1
        #     if s>0:
        #         return  best_profit(s,profit,prices)
        #     return profit

        
        # return best_profit(len(prices)-1,profit,prices)
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            # update minPrice if we find a smaller price
            if price < minPrice:
                minPrice = price
            # check profit if we sell today
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit



                        

        