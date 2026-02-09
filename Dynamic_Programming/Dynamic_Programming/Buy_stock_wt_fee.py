# You are given an array arr[], in which arr[i] is the price of a given stock on the ith day and an integer k represents 
# a transaction fee. Find the maximum profit you can achieve. You may complete as many transactions as you like, but you 
# need to pay the transaction fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Input: arr[] = [6, 1, 7, 2, 8, 4], k = 2
# Output: 8
# Explanation:
# Buy the stock on day 2 and sell it on day 3 => 7 – 1 -2 = 4
# Buy the stock on day 4 and sell it on day 5 => 8 – 2 - 2 = 4
# Maximum Profit  = 4 + 4 = 8


class Solution:
    def maxProfit(self,arr,k):
        #Code here
        cash = 0
        hold = -arr[0]
        for price in arr[1:]:
            cash = max(cash, hold+price-k)
            hold = max(hold, cash - price)
        return cash
    
arr = [1, 3, 2, 8, 4, 9]
k = 2
sol = Solution()
result = sol.maxProfit(arr, k)
print(result)