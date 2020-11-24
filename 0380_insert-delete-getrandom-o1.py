"""
常数时间插入、删除和获取随机元素

标签：设计问题

链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1

设计一个支持在平均时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

示例 :
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();

我的解题思路：
1. 字典。(获取随机数的时间复杂度不是 O(1))

官方解法：
1. 哈希表 + 动态数组。
哈希表存放 val 和 val 在数组里的下标索引，
数组存放 val，
删除元素时，将数组最后一位 last_element 移到 val 的位置，并更新哈希表中 last_element 的值为 val 的位置下标，
再直接删除数组最后一位，就相当于用 O(1) 的时间删除了 val。

时间复杂度：getRandom 时间复杂度为 O(1)，
 - insert 和 remove 平均时间复杂度为 O(1)，
   在最坏情况下为 O(N) 当元素数量超过当前分配的动态数组和哈希表的容量导致空间重新分配时。
空间复杂度：O(N)，在动态数组和哈希表分别存储了 N 个元素的信息。

"""
import random
import unittest


class RandomizedSet:
    """哈希表 + 动态数组。"""
    
    def __init__(self):
        self.dict = {}
        self.arr = []
    
    def insert(self, val: int) -> bool:
        """
        将元素添加到动态数组，
        将元素添加到哈希表，键为元素，值为元素在动态数组的下标。
        """
        if val in self.dict:
            return False
        
        # 下标为 len(self.arr) - 1，所以先存字典。
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        """
        从哈希表中找出待删除元素在动态数组中的下标，
        交换动态数组中目标元素与最后一个元素的位置，并删除最后一个元素，
        更新哈希表中被交换元素的值（下标）。
        """
        if val not in self.dict:
            return False
        
        # 找出待删除元素的下标，最后一个元素。
        idx, last_element = self.dict[val], self.arr[-1]
        # 将待删除元素变成最后一个元素。
        self.arr[idx] = last_element
        # 更新被交换后的最后一个元素下标。
        self.dict[last_element] = idx
        # 删除最后一个元素。
        self.arr.pop()
        del self.dict[val]
        return True
    
    def getRandom(self) -> int:
        """
        从动态数组从随机返回一个数。
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class TestRandomizedSet(unittest.TestCase):
    def setUp(self) -> None:
        self.r = RandomizedSet()

    def test_insert(self) -> None:
        self.assertTrue(
            self.r.insert(1)
        )

    def test_remove(self) -> None:
        self.assertFalse(
            self.r.remove(1)
        )

    def test_get_random(self) -> None:
        self.r.insert(2)
        self.assertEqual(
            self.r.get_random(),
            2,
        )


if __name__ == '__main__':
    unittest.main()
