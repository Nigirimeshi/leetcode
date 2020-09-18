"""
Fizz Buzz

标签：数学

链接：https://leetcode-cn.com/problems/fizz-buzz

写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是 3 的倍数，输出 “Fizz”；
2. 如果 n 是 5 的倍数，输出 “Buzz”；
3.如果 n 同时是 3 和 5 的倍数，输出 “FizzBuzz”。

示例：
n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

我的解题思路：
1. 如题模拟一遍。

官方解法：
1. 散列表。
算法：
1) 把所有的映射关系放在散列表 fizzBuzzHash 中，这个散列表形如 { 3: 'Fizz', 5: 'Buzz' }。
2) 遍历 1 ... N1...N。
3) 对于每个数字，遍历 fizzBuzzHash 中的键，检查是否能被它整除。
4) 如果这个数能被键整除，就把当前键映射的值加到到答案字符串后面去。对于散列表的每个键值对，都这样操作。
5) 最后将答案字符串加入答案列表。

时间复杂度： O(N)
空间复杂度： O(1)

"""
import unittest
from typing import List


class Solution:
    def fizz_buzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


class OfficialSolution:
    def fizz_buzz(self, n: int) -> List[str]:
        ans = []
        fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}

        for i in range(1, n + 1):
            tmp = ''
            for k in fizz_buzz_dict.keys():
                if i % k == 0:
                    tmp += fizz_buzz_dict[k]

            if not tmp:
                tmp = str(i)

            ans.append(tmp)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_fuzz_buzz(self) -> None:
        self.assertListEqual(
            self.s.fizz_buzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz"
            ]
        )


if __name__ == '__main__':
    unittest.main()
