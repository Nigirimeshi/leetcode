"""
任务调度器

链接：https://leetcode-cn.com/problems/task-scheduler

给定一个用字符数组表示的 CPU 需要执行的任务列表。
其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 ：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。

提示：
任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

官方解法：
1. 桶。
使用桶思想，建立大小为 n + 1 的桶子，桶的数量为最多的那个任务。
比如，等待时间为 n = 2，A 任务数量为 6，我们可以建立 6 个桶子，每个容量为 3。
有以下几种情况：
1) 任务 A 数量是最多的，其他任务数量都比 A 小，那么完成任务 A 所需的时间应是 (6-1) * 3 + 1 = 16，因为最后一个桶子，不存在等待时间。
2) 存在任务 B 和任务 A 的数量相同，那么完成 A 所需时间应是 (6-1) * 3 + 2 = 17。
前 2 种情况，总结一下，总时间 = (桶个数 - 1) * (n + 1) + 最后一桶的任务数量。
3) 当冷却时间 n 较小，任务种类很多时，这种情况实际上每个任务间都不存在空余时间，总时间就等于任务数量。

总结以上情况，只需要计算 2 个数：
1) 记录最大任务数量 N，看一下任务数量并列最多的有几个，即最后一桶的任务数量 X，再计算 num1 = (N-1) * (n+1) + X
2) num2 = tasks.size()
最后返回其中较大值即可，因为存在空闲时间时肯定 num1 大，不存在空闲时间时 num2>=num1。

时间复杂度：O(nlogn)。
空间复杂度：O(1)。

"""
import collections
import unittest
from typing import List


class OfficialSolution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        """桶。"""
        # 统计各任务次数。
        counts = collections.Counter(tasks)
        # 获取出现次数最多的任务数量。
        max_count = max(counts.values())
        # 任务数量并列最多的有几个。
        tasks_nums = collections.Counter(counts.values()).get(max_count)
        # num1 = (桶数量 - 1) * (n + 1) + 最后一个桶的任务数量。
        res = (max_count - 1) * (n + 1) + tasks_nums
        size = len(tasks)
        return max(res, size)


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()

    def test_least_interval(self) -> None:
        self.assertEqual(
            self.s.least_interval(["A", "A", "A", "B", "B", "B"], 2),
            8,
        )


if __name__ == '__main__':
    unittest.main()
