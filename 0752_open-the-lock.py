"""
打开转盘锁

链接：https://leetcode-cn.com/problems/open-the-lock

你有一个带有四个圆形拨轮的转盘锁。

每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。

每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。

每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2:
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。

示例 3:
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
示例 4:

输入: deadends = ["0000"], target = "8888"
输出：-1

提示：
死亡列表 deadends 的长度范围为 [1, 500]。
目标数字 target 不会在 deadends 之中。
每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。

解法：
1. BFS。


"""
import unittest
from collections import deque
from typing import Iterator, List


class Solution:
    def open_lock(self, deadends: List[str], target: str) -> int:
        """BFS。"""
        # 初始队列，起始数字是 0000，旋转次数为 0。
        queue = deque([("0000", 0)])
        # 存储已访问过的数字。
        seen = {"0000"}
        while queue:
            node, depth = queue.popleft()

            # 刚好等于目标值，返回旋转次数（树的深度）。
            if node == target:
                return depth
            # 死亡数字，跳过。
            if node in deadends:
                continue

            # 遍历所有子节点。
            # 4 位数字，分别支持上、下旋转，共 8 种可能，即 8 个子节点。
            for child in self.neighbors(node):
                # 已访问过的数字，跳过。
                if child in seen:
                    continue

                # 加入队列。
                queue.append((child, depth + 1))
                # 标记已访问。
                seen.add(child)
        # 无法解锁。
        return -1

    def neighbors(self, node: str) -> Iterator[str]:
        # 4 位数字。
        for i in range(len(node)):
            # 第 i 位数字。
            num = int(node[i])
            # 上、下拨动。
            for x in [-1, 1]:
                if x == -1 and num == 0:
                    n = 9
                elif x == 1 and num == 9:
                    n = 0
                else:
                    n = num + x

                yield node[:i] + str(n) + node[i + 1 :]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_open_lock(self) -> None:
        self.assertEqual(
            6,
            self.s.open_lock(
                ["0201", "0101", "0102", "1212", "2002"],
                "0202",
            ),
        )
        self.assertEqual(
            1,
            self.s.open_lock(
                ["8888"],
                "0009",
            ),
        )
        self.assertEqual(
            -1,
            self.s.open_lock(
                ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                "8888",
            ),
        )


if __name__ == "__main__":
    unittest.main()
