"""
第一个错误的版本

链接：https://leetcode-cn.com/problems/first-bad-version

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。

我的解题思路：
1. 暴力搜索。(超时了)

2. 二分搜索。


官方解法：
1. 二分查找。
场景一：isBadVersion(mid) => false

 1 2 3 4 5 6 7 8 9
 G G G G G G B B B       G = 正确版本，B = 错误版本
 |       |       |
left    mid    right

场景一中，isBadVersion(mid) 返回 false，因此我们知道 mid 左侧（包括自身）的所有版本都是正确的。
所以我们令 left = mid + 1，把下一次的搜索空间变为 [mid+1, right]。

场景二：isBadVersion(mid) => true

 1 2 3 4 5 6 7 8 9
 G G G B B B B B B       G = 正确版本，B = 错误版本
 |       |       |
left    mid    right

场景二中，isBadVersion(mid) 返回 true，因此我们知道 mid 右侧（不包括自身）的所有版本的不可能是第一个错误的版本。
所以我们令 right=mid，把下一次的搜索空间变为 [left, mid]。

在二分查找的每次操作中，我们都用 left 和 right 表示搜索空间的左右边界，因此在初始化时，需要将 left 的值设置为 1，并将 right 的值设置为 n。
当某一次操作后，left 和 right 的值相等，此时它们就表示了第一个错误版本的位置。可以用数学归纳法 证明二分查找算法的正确性。

在二分查找中，选取 mid 的方法一般为 mid = 1//2 * (left+right)。
如果使用的编程语言会有整数溢出的情况（例如 C++，Java），那么可以用 mid = left + 1//2 * (right−left) 代替前者。

时间复杂度：O(logn)。搜索空间每次减少一半，因此时间复杂度为 O(logn)。
空间复杂度：O(1)。

"""
import unittest


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True if version >= 3 else False


class Solution:
    def first_bad_version(self, n: int) -> int:
        """暴力搜索。（超时了）"""
        if n == 1:
            return 1

        prev = isBadVersion(n)
        for i in range(n - 1, 0, -1):
            now = isBadVersion(i)
            if prev != now:
                return i + 1
            prev = now
        return 1

    def first_bad_version_2(self, n: int) -> int:
        """二分搜索。"""
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    unittest.main()
