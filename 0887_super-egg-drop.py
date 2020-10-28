"""
鸡蛋掉落

链接：https://leetcode-cn.com/problems/super-egg-drop

你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N 共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

示例 1：
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

示例 2：
输入：K = 2, N = 6
输出：3

示例 3：
输入：K = 3, N = 14
输出：4

提示：
1 <= K <= 100
1 <= N <= 10000

官方解法：
1. 动态规划。（提交超时）
状态：即当前拥有的鸡蛋个数 K 和需要测试楼层数 N。随着测试进行，鸡蛋个数会减少，楼层的搜索范围会减少。

选择在第 i 层扔鸡蛋，存在两种可能情况：
 - 如果鸡蛋碎了，那么鸡蛋的个数 K 应该减一，搜索的楼层应该从 [1, N] 变成 [1, i - 1]，共 i - 1 层。
 - 如果鸡蛋没碎，那么鸡蛋的个数不变，搜索的楼层应该从 [1, N] 变成 [i + 1, N]，共 N - i 层。

鸡蛋是碎了还是没碎，取决于哪种情况下尝试次数更多，因为我们想求的是最坏情况下的结果。

时间复杂度：O(K*N^2)
空间复杂度：O(KN)

2. 动态规划 + 二分搜索。
能用二分搜索是因为状态转移方程的函数图像具有单调性，可以快速找到最值。

根据 dp(k, n) 数组的定义，当 k 固定时，随着 n 的增加，该函数一定是单调递增的。
那么注意 dp(k-1, i-1) 和 dp(k, n-i) 这两个函数，其中 i 是从 1 到 N 单增的，如果固定了 k 和 n，把它们看成关于 i 的函数，
前者随着 i 的增加是单增的，后者随着 i 的增加是递减的。
这时求两者的较大值，再求较大值中的最小值，相当于求这两条直线的交点。

时间复杂度：O(K*N*logN)
空间复杂度：O(KN)

"""
import unittest


class Solution:
    def super_egg_drop(self, K: int, N: int) -> int:
        """动态规划。"""
        memo = {}
        
        def dp(k, n: int) -> int:
            # 只有一个蛋，只能一层层试。
            if k == 1:
                return n
            if n == 0:
                return 0
            
            # 避免重复计算子问题。
            if (k, n) in memo:
                return memo[(k, n)]
            
            res = float('INF')
            for i in range(1, n + 1):
                res = min(
                    res,
                    max(
                        dp(k - 1, i - 1),  # 蛋碎了，蛋数量 -1；去 0 到 i - 1 层继续试。
                        dp(k, n - i),  # 蛋没碎，蛋的数量不变；向上递归后，第 i 层相当于第 0 层，因此接着去 0 到 n - i 层继续试。
                    ) + 1,  # 第 i 楼扔了一次。
                )
            
            # 记录备忘录。
            memo[(k, n)] = res
            return res
        
        return dp(K, N)
    
    def super_egg_drop_2(self, K: int, N: int) -> int:
        """动态规划 + 二分搜索。"""
        memo = {}
        
        def dp(k, n: int) -> int:
            if k == 1:
                return n
            if n == 0:
                return 0
            
            if (k, n) in memo:
                return memo[(k, n)]
            
            res = float('INF')
            # 用二分搜索代替线性搜索。
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                broken = dp(k - 1, mid - 1)  # 蛋碎了。
                not_broken = dp(k, n - mid)  # 蛋没碎。
                if broken > not_broken:
                    right = mid - 1
                    res = min(res, broken + 1)
                else:
                    left = mid + 1
                    res = min(res, not_broken + 1)
            
            # 记录，避免重复计算。
            memo[(k, n)] = res
            return res
        
        return dp(K, N)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_super_egg_drop(self):
        self.assertEqual(
            self.s.super_egg_drop_2(1, 2),
            2,
        )
        self.assertEqual(
            self.s.super_egg_drop_2(2, 6),
            3,
        )
        self.assertEqual(
            self.s.super_egg_drop_2(3, 14),
            4,
        )
        self.assertEqual(
            self.s.super_egg_drop_2(4, 2000),
            16,
        )


if __name__ == '__main__':
    unittest.main()
