"""
滑动窗口最大值

链接：https://leetcode-cn.com/problems/sliding-window-maximum

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length


我的解题思路：
1. 暴力法。（提交超时）
设 i 从 0 遍历到 len(nums) - k，每次记录 nums[i] 到 nums[i+k-1] 区间内的最大值。

时间复杂度：O(nk)
空间复杂度：O(n-k+1) 存储输出数组。

官方解法：
1. 单调（递减）双向队列。
双向队列可以从两端以常数时间压入/弹出元素。

每个窗口前进的时候，要添加一个数同时减少一个数，所以想在 O(1) 的时间得出新的最值，就需要「单调队列」这种特殊的数据结构来辅助。

一个普通的队列一定具备 push 和 pop 操作：
class Queue:
    def push(n):  # 或 enqueue，在队尾加入元素 n。
        pass
    
    def pop():  # 或 dequeue，删除队头元素。
        pass

一个单调队列的操作也类似：
class MonotonicQueue:
    def push(n):  # 在队尾加入元素 n。
        pass
    
    def pop(n):  # 队头元素如果是 n，删除它。
        pass

    def max():  # 返回当前队列中元素的最大值。
        pass

「单调队列」的核心思路和「单调栈」类似。单调队列的 push 方法依然在队尾添加元素，
但是要把前面比新元素小的元素都删掉，如果每个元素被加入时都这样操作，最终单调队列中的元素大小就会保持一个单调递减的顺序。

时间复杂度：O(n)
空间复杂度：O(n) 输出数组使用了 O(n-k+1) 空间，双向队列使用了 O(k)

2. 动态规划。


"""
from collections import deque
from typing import List
import unittest


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """暴力。"""
        n = len(nums)
        
        # nums 长度或 k 为 0，无需求解。
        if n * k == 0:
            return []
        
        return [max(nums[i:i + k]) for i in range(0, n - k + 1)]


class MonotonicQueue:
    def __init__(self):
        self.deque = deque()
    
    def push(self, n: int) -> None:
        # 在队尾加入元素前，先把前面比 n 小的元素都删除。
        while len(self.deque) > 0 and self.deque[-1] < n:
            self.deque.pop()
        self.deque.append(n)
    
    def pop(self, n: int) -> None:
        # 由于 push 操作，比 n 小的数字可能已经被删除了，所以如果队列头元素等于 n，才删除它。
        if len(self.deque) > 0 and self.deque[0] == n:
            self.deque.popleft()
    
    def max(self) -> int:
        # 由于双向队列递减，所以头元素即为最大值。
        return self.deque[0]


class OfficialSolution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """单调（递减）双向队列。"""
        # 实例化单调递减双向队列。
        window = MonotonicQueue()
        # 存放结果。
        ans = []
        for i in range(len(nums)):
            # 先填满窗口的前 k - 1 个。
            if i < (k - 1):
                window.push(nums[i])
            
            # 窗口向右滑动。
            else:
                # 加入新的元素。
                window.push(nums[i])
                # 记录本次滑动窗口的最大值。
                ans.append(window.max())
                # 检测是否需要删除窗口最左元素。
                window.pop(nums[i - k + 1])
        
        return ans
    
    def max_sliding_window_2(self, nums: List[int], k: int) -> List[int]:
        """动态规划。"""


class TestOfficialSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = OfficialSolution()
    
    def test_max_sliding_window(self) -> None:
        self.assertListEqual(
            self.s.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )


if __name__ == '__main__':
    unittest.main()
