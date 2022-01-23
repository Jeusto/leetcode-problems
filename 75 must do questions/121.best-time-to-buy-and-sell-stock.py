#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    minimum_price = prices[0]
    current_max_profit = 0

    for i in range(len(prices)):
      if prices[i] < minimum_price:
        minimum_price = prices[i]
      elif prices[i] - minimum_price > current_max_profit:
        current_max_profit = prices[i] - minimum_price

    return current_max_profit


# @lc code=end