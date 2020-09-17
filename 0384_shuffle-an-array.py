"""
打乱数组

类型：设计问题

链接：https://leetcode-cn.com/problems/shuffle-an-array

打乱一个没有重复元素的数组。

示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

我的解题思路：
1. 随机交换数组里的 2 个元素。

官方解法：
1. 暴力。
暴力算法简单的来说就是把每个数放在一个 ”帽子“ 里面，每次从 ”帽子“ 里面随机摸一个数出来，直到 “帽子” 为空。

时间复杂度： O(n^2)
乘方时间复杂度来自于 list.remove（list.pop）。每次操作都是线性时间的，总共发生 n 次。

空间复杂度： O(n)
因为需要实现重置方法，需要额外的空间把原始数组另存一份，在重置的时候用来恢复原始状态。

2. Fisher-Yates 洗牌算法。
Fisher-Yates 洗牌算法跟暴力算法很像。
在每次迭代中，生成一个范围在当前下标到数组末尾元素下标之间的随机整数。
接下来，将当前元素和随机选出的下标所指的元素互相交换；
这一步模拟了每次从 “帽子” 里面摸一个元素的过程，其中选取下标范围的依据在于每个被摸出的元素都不可能再被摸出来了。
此外还有一个需要注意的细节，当前元素是可以和它本身互相交换的 - 否则生成最后的排列组合的概率就不对了。

时间复杂度 ： O(n)
Fisher-Yates 洗牌算法时间复杂度是线性的，因为算法中生成随机序列，交换两个元素这两种操作都是常数时间复杂度的。

空间复杂度： O(n)
因为要实现 重置 功能，原始数组必须得保存一份，因此空间复杂度并没有优化。

"""
import unittest
import random
from typing import List


class OfficialSolution:
    """暴力。"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        self.original = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        aux = self.nums.copy()
        for i in range(len(self.nums)):
            remove_idx = random.randrange(len(aux))
            self.nums[i] = aux.pop(remove_idx)
        return self.nums


class OfficialSolution2:
    """Fisher-Yates 洗牌算法。"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        self.original = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        size = len(self.nums)
        for i in range(size):
            random_idx = random.randrange(i, size)
            self.nums[i], self.nums[random_idx] = self.nums[random_idx], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    unittest.main()
