"""
最小栈

类型：设计问题

链接：https://leetcode-cn.com/problems/min-stack

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:
输入：
["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]

输出：
[null, null, null, null, -3, null, 0, -2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。

我的解题思路：
1. 用数组存储元素。
push 相当于 append
pop  相当于 pop
top  相当于 array[-1]
getMin 比较特殊，题目要求常数时间内检索，所以需要单独维护一个变量 min_num；
每次 push 时，min_num = min(min_num, num)
每次 pop 时，若移出的元素等于 min_num，则根据现有现有重新计算 min_num。

官方解法：
1. 辅助栈。
用 stack 存储元素，用 min_stack 存储每个元素对应的最小值。
元素栈中每个元素 x 与辅助栈中对应的最小值时刻保持对应。
辅助栈与元素栈同步插入和删除，用于存储每个元素对应的最小值。

"""
import math
import unittest


class MinStack:

    def __init__(self):
        self.array = []
        self.min = None

    def push(self, x: int) -> None:
        self.array.append(x)

        if self.min is None:
            self.min = x
        else:
            self.min = min(self.min, x)

    def pop(self) -> None:
        tmp = self.array[-1]
        self.array.pop()

        if tmp == self.min:
            sorted_array = sorted(self.array)
            if not sorted_array:
                self.min = None
            else:
                self.min = sorted_array[0]

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min


class OfficialMinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    unittest.main()
