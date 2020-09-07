"""
验证回文串

链接：https://leetcode-cn.com/problems/valid-palindrome

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

我的解题方案：
1.
遍历字符串，清理字符串：仅保留字母和数字，大写转小写，清理后的字符串长度为 n；
设置左右指针，左值针从 0 递增至；右指针从 n - 1 递减；
遍历清理后的字符串，左右指针指向元素不等时，返回 False，左指针下标 >= 右指针时退出循环。
时间复杂度：O(|s|)，其中 |s| 是字符串 s 的长度。
空间复杂度：O(|s|)。由于我们需要将所有的字母和数字字符存放在另一个字符串中，在最坏情况下，新的字符串 ss 与原字符串 s 完全相同，因此需要使用 O(|s|) 的空间。

官方解法：
2. 在字符串上使用双指针。
在移动左右指针时，需要不断向另一指针的方向移动，直到遇到一个字母或数字时，或两指针重合时停止。
也就是说，每次先将两个指针移动到下一位置，再判断是否相等。
时间复杂度：O(|s|)，其中 |s| 是字符串 s 的长度。
空间复杂度：O(1)。
"""
import unittest


class Solution:
    def is_palindrome(self, s: str) -> bool:
        ss = ''.join(c.lower() for c in s if c.isalnum())

        n = len(ss)
        left, right = 0, n - 1

        while left < right:
            if ss[left] != ss[right]:
                return False
            left, right = left + 1, right - 1
        return True


class OfficialSolution:
    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if left < right:
                if s[left].lower() != s[right].lower():
                    return False

                left, right = left + 1, right - 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_palindrome(self) -> None:
        self.assertTrue(
            self.s.is_palindrome('A man, a plan, a canal: Panama')
        )


if __name__ == '__main__':
    unittest.main()
