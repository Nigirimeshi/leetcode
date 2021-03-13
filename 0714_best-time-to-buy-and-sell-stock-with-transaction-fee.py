"""
买卖股票的最佳时机含手续费

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

解法：
1. 动态规划（状态机）

"""
import unittest
from typing import List


class Solution:
    def max_profit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float("-inf")
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)  # 每次卖出时交手续费。
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0


class Cases:
    def __init__(self, prices: List[int], fee: int, want: int):
        self.prices: List[int] = prices
        self.fee: int = fee
        self.want: int = want


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_max_profit(self):
        test_cases = (Cases([1, 3, 2, 8, 4, 9], 2, 8),)

        for tc in test_cases:
            output = self.s.max_profit(tc.prices, tc.fee)
            self.assertEqual(tc.want, output)


if __name__ == "__main__":
    unittest.main()
