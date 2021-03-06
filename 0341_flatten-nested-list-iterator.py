"""
扁平化嵌套列表迭代器

链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator

给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:
输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。

示例 2:
输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

官方解法：
1. 栈。
初始化栈：题目要求从左到右输出数字，因为栈 pop 从右端开始，所以压栈时需将 nestedList 反转再入栈。
当栈顶元素为数字时，next() 直接返回即可;
当栈顶元素为列表时，弹出该元素，并将其反转再次入栈。


"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger():
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
    
    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
    
    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 题目要求从左到右输出数字，但栈 pop 从右端开始，所以需要将 nestedList 反转再入栈。
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # 因为 hasNext 确保了扎顶元素为数字，所以直接弹出栈顶元素即可。
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # 当栈顶不为空，且栈顶元素为列表时，将其弹出反转后再入栈。
        while len(self.stack) > 0 and self.stack[-1].isInteger() is False:
            self.stack += self.stack.pop().getList()[::-1]
        return len(self.stack) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
