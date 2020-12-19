"""
零钱兑换

标签：动态规划

链接：https://leetcode-cn.com/problems/coin-change

给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


官方解法：
1. 动态规划 - 至下而上。
dp[i] 为组成金额 i 所需最少的硬币数量。在计算 dp[i] 之前已经得到 dp[0] ~ dp[i-1] 的值。

状态转移方程：dp[i] = min(dp[i - coins[j]]) + 1; coins[j] 代表第 j 枚硬币的面值。
边界条件：dp[0] = 0，当 i 小于 0 时，忽略 dp[i]。

例子 1：假设 coins = [1, 2, 5]，amount = 11。
dp[i]   最小硬币数量
dp[0]   0   // 没有硬币能够组合成金额 0。
dp[1]   1   // dp[1] = min(dp[1-1], dp[1-2], dp[1-5]) + 1 = dp[0] + 1 = 1
dp[2]   1   // dp[2] = min(dp[2-1], dp[2-2], dp[2-5]) + 1 = min(dp[1], dp[0]) + 1 = 1
dp[3]   2   // dp[3] = min(dp[3-1], dp[3-2], dp[3-5]) + 1 = min(dp[2], dp[1]) + 1 = 2
...
dp[11]  3   // dp[11] = min(dp[11-1], dp[11-2], dp[11-5]) + 1 = 3

时间复杂度：O(S*N)。S 是金额树，N 是金币面额数量。
空间复杂度：O(S)。dp 数组占用。

"""
from typing import List
import unittest


class OfficialSolution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        """动态规划 - 至下而上。"""
        # 求最小值，初始值用最大值。
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
    
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
    
        return dp[amount] if dp[amount] != float('inf') else -1

    def coin_change_2(self, coins: List[int], amount: int) -> int:
        """
        动态规划（自底向上）。
        1. base case。
           amount 为 0 时，所需硬币数量为 0。
        2. 状态。
           amount。
        3. 选择。
           coins。
        4. dp 数组/方程。
           dp[n] = 凑成金额 n 最少需要多少硬币。
        """
        # dp 数组大小为 amount + 1，初始值也为 amount + 1。
        # 因为凑成 amount 的硬币最多只能等于 amount，用 amount + 1 相当于初始化正无穷，便于后续取最小值。
        dp = [amount + 1] * (amount + 1)
        # base case。
        dp[0] = 0
        # 循环所有状态的取值 [0, amount]。
        for i in range(amount + 1):
            # 循环求所有选择的最小值。
            for coin in coins:
                # 子问题无解，跳过。
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
        return dp[amount] if dp[amount] != (amount + 1) else - 1


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_coin_change(self) -> None:
        self.assertEqual(
            self.s.coin_change([1, 2, 5], 11),
            3,
        )


if __name__ == '__main__':
    unittest.main()
