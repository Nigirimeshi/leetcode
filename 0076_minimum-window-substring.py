"""
最小覆盖子串

链接：https://leetcode-cn.com/problems/minimum-window-substring

给你一个字符串 s 、一个字符串 t 。

返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：
输入：s = "a", t = "a"
输出："a"

提示：
1 <= s.length, t.length <= 105
s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

解法：
1. 滑动窗口。


"""
import unittest
from collections import defaultdict
from typing import Dict


class Solution:
    def min_window(self, s: str, t: str) -> str:
        """滑动窗口。"""
        need: Dict[str, int] = defaultdict(int)
        window: Dict[str, int] = defaultdict(int)

        # 初始化窗口。
        for c in t:
            need[c] += 1

        # 窗口指针。
        left, right = 0, 0
        # 最小覆盖子串起始、结束下标。
        start, end = 0, len(s)  # 注意：起始 end 下标超过 s 的有效索引下标。
        # 每当 window 和 need 对应字符数相同时，加一；反之减一。
        valid = 0
        while right < len(s):
            # 待移入窗口的字符。
            c = s[right]
            # 扩大窗口，移动右指针。
            right += 1
            # 字符在 t 中。
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 需要缩小窗口。
            while valid == len(need):
                # 当当前窗口大小比最小覆盖子串长度小时，更新其下标。
                # right - 1 是因为上面先加了 1。
                if (right - 1 - left) < (end - start):
                    start, end = left, right - 1

                # 待移出窗口的字符。
                d = s[left]
                # 缩小窗口，移动左值针。
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        # window 中对应字符的数量与 need 即将不匹配（不满足缩小窗口的条件了）。
                        valid -= 1
                    window[d] -= 1

        # 最小覆盖子串结尾下标和 s 长度相同，说明 end 没变过，即不存在最小覆盖子串。
        if end == len(s):
            return ""
        return s[start : end + 1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_min_window(self) -> None:
        self.assertEqual("BANC", self.s.min_window("ADOBECODEBANC", "ABC"))


if __name__ == "__main__":
    unittest.main()
