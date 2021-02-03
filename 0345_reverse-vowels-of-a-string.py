"""
反转字符串中的元音字母。

链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：

输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

提示：
元音字母不包含字母 "y" 。

我的解题思路：
1. 双指针。
设置 left，right 指针分别指向字符串的头部和尾部。
使 left 右移并跳过非元音字母，使 right 左移并跳过非原因字母，
交换 left 和 right。

时间复杂度：O(N)
空间复杂度：O(N)

"""
import unittest


class Solution:
    def reverse_vowels(self, s: str) -> str:
        """双指针。"""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        arr = list(s)
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left].lower() not in vowels:
                left += 1
                continue
            if arr[right].lower() not in vowels:
                right -= 1
                continue
            
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
        return ''.join(arr)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
    
    def test_reverse_vowels(self) -> None:
        self.assertEqual(
            self.s.reverse_vowels('leetcode'),
            'leotcede'
        )


if __name__ == '__main__':
    unittest.main()
