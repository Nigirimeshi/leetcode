"""
编辑距离

链接：https://leetcode-cn.com/problems/edit-distance

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

官方解法：
1. 动态规划（自底向上）。
状态：dp[i][j] 代表 word1 从位置 i 转换成 word2 的位置 j 需要的最少步数。
条件：
 - 当 word1[i] == word2[j] 时，不需要转换，所以 dp[i][j] = dp[i-1][j-1]。
 - 当 word2[i] != word2[j] 时，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，
   即左上方，上方，左边相邻状态的最小值 + 1，
   dp[i-1][j-1] 表示替换，dp[i-1][j] 表示删除，dp[i][j-1] 表示插入。
特例：
 - dp 第一行、第一列要单独考虑，引入 ''，如下：
       ‘’  r  o  s
   ‘’  0   1  2  3
   h   1
   o   2
   r   3
   s   4
   e   5
   第一行，是 word1 为空，变成 word2 所需的最少步数，即插入。
   第一列，是 word2 为空，word1 变成空字符串所需的最少步数，即删除。
   

"""
import unittest


class OfficialSolution:
    def min_distance(self, word1: str, word2: str) -> int:
        """动态规划（自底向上）。"""
        m, n = len(word1), len(word2)
        # 把一个单词变成另一个单词，最多等于其中较长单词的长度。
        max_len = max(m, n)
        dp = [[max_len for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始化第一列。
        for i in range(m + 1):
            dp[i][0] = i
        # 初始化第一行。
        for i in range(n + 1):
            dp[0][i] = i
        
        # 状态转移，第一行和第一列已初始化，所以行和列下标从 1 开始。
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # word1 和 word2 字符相同，不需要转换，dp 等于上一次最少需要的步数。
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # word1 和 word2 字符不同，dp 等于替换、删除、插入 3 种操作中的最少值 + 1。
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_climb_stairs(self) -> None:
        self.assertEqual(
            self.s.min_distance('horse', 'ros'),
            3
        )
        self.assertEqual(
            self.s.min_distance('intention', 'execution'),
            5
        )


if __name__ == '__main__':
    unittest.main()
