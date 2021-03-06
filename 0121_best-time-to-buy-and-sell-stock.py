"""
买卖股票的最佳时机

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


官方解法：
1. 动态规划。
dp[i] 表示前 i 天的最大利润，因为始终需要保持利益最大化，所以可得规则：
dp[i] = max(dp[i-1], prices[i] - min_price)

时间复杂度：O(n)
空间复杂度：O(n)

2. 动态规划（一次遍历，优化空间）。
时间复杂度：O(n)
空间复杂度：O(1)

"""
import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """动态规划。"""
        n = len(prices)
        if n == 0:
            return 0

        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
        return dp[-1]

    def max_profit_2(self, prices: List[int]) -> int:
        """动态规划（一次遍历，优化空间）。"""
        min_price, max_price = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        return max_price


if __name__ == '__main__':
    unittest.main()
