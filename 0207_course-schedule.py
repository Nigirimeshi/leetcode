"""
课程表

链接：https://leetcode-cn.com/problems/course-schedule

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。

先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，

表示如果要学习课程 ai 则必须先学习课程 bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

提示：
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对互不相同。

解法：
1. 拓扑排序 - DFS。
通过 DFS 判断图中是否有环。

算法：
1）使用标记列表 flags，用于记录和判断每个节点 i 的状态：
1.1）未被 DFS 访问的节点 flags[i] = 0；
1.2）已被其他节点的 DFS 访问过 flags[i] = -1；
1.3）已被当前节点的 DFS 访问过 flags[i] = 1，存在环。
2）对给定的节点列表依次执行 DFS，判断每个节点 DFS 是否存在环，存在就立即返回 False。
2.1）DFS 流程：
2.1.1）终止条件：
       - 当 flags[i] = -1 时，说明当前节点已被其他节点访问过，无需重复搜索，返回 True。
       - 当 flags[i] = 1 时，说明本轮 DFS 中节点 i 被第 2 次访问，即存在环，直接返回 False。
2.1.2）将当前访问节点 i 对应的 flags[i] 置 1，即标记其本轮被访问过。
2.1.3）递归访问当前节点的所有邻接节点 j，发现环时直接返回 False。
2.1.4）当前节点的所有邻接节点都被遍历过了，且没有发现环，则将当前节点 flag 置为 -1，并返回 True。
3）整个图遍历完了也没发现环，返回 True。

时间复杂度：O(N+M)，遍历图需要访问所有节点和邻边，N 是节点数量，M 是邻边数量。
空间复杂度：O(N+M)，建立邻接表需要的空间，adjacency 长为 N，存储了 M 条邻边的数据。

2. 入度表 - BFS。
算法：
1）统计每个课程的入度，生成入度表（indegress）。
2）使用队列（queue），将入度为 0 的节点入队。
3）当队列（queue）非空时，依次将队首节点出队，并在课程安排图中删除该节点（prev）：
3.1）并不是真的删除，而是通过将此节点（prev）的所有邻接节点（curr）的入度 - 1，即 indegress[curr] -= 1。
3.2）当入度 - 1 后，邻接节点的入度若为 0，则说明 curr 的所有的前驱节点已被 “删除”，此时将 curr 入队。
4）在每次 prev 出队时，使 numCourses - 1，
   - 若整个课程安排表是有向无环图，则所有节点一定都入队和出队过，即完成拓扑排序过。
     换句话说，若图中存在环，一定有节点的入度始终不为 0。
   - 因此，拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断是否存在环。
   
时间复杂度：O(N+M)，历一个图需要访问所有节点和所有临边，N 和 M 分别为节点数量和临边数量。
空间复杂度：O(N+M)，为建立邻接表所需额外空间，adjacency 长度为 N ，并存储 M 条临边的数据。

"""
import unittest
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 邻接表，下标对应需要先修的课程，值中存放修完该课程后，可修的课程列表。
        adjacency: List[List[int]] = [[] for _ in range(numCourses)]
        # 构建邻接表。
        for curr, prev in prerequisites:
            adjacency[prev].append(curr)

        # 各课程的标记：
        #  0 表示未被 DFS 访问过。
        # -1 表示被其他节点 DFS 访问过。
        #  1 表示已被当前节点 DFS 访问过。
        flags: List[int] = [0] * numCourses
        # DFS 遍历各节点。
        for i in range(numCourses):
            if not self.dfs(i, adjacency, flags):
                return False

        # 没有环。
        return True

    def dfs(self, i: int, adjacency: List[List[int]], flags: List[int]) -> bool:
        # 已被其他节点 DFS 遍历过。
        if flags[i] == -1:
            return True
        # 已被当前节点 DFS 遍历过，存在环。
        if flags[i] == 1:
            return False

        # 正在遍历当前节点，标记位置为 1。
        flags[i] = 1
        # 递归遍历邻接节点。
        for j in adjacency[i]:
            if not self.dfs(j, adjacency, flags):
                return False
        # 遍历过当前节点，标记位置为 -1。
        flags[i] = -1
        # 当前节点及其邻接节点，不存在环。
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化入度表。
        indegress: List[int] = [0] * numCourses
        # 初始化邻接表。
        adjacency: List[List[int]] = [[] for _ in range(numCourses)]
        # 初始化入度表，邻接表。
        for curr, prev in prerequisites:
            indegress[curr] += 1
            adjacency[prev].append(curr)

        # 初始化队列。
        queue = deque()
        # 将入度为 0 的节点入队。
        for i in range(len(indegress)):
            if indegress[i] == 0:
                queue.append(i)

        while queue:
            prev = deque.popleft()
            # 将该节点的所有邻接节点的入度 - 1。
            for curr in adjacency[prev]:
                indegress[curr] -= 1
                # 若邻接节点的入度变为 0，说明其不存在前驱节点了，则将其加入队列。
                if indegress[curr] == 0:
                    queue.append(curr)

            # 每出队一个节点，就使 numCourses - 1，不存在环时，出队次数应等于课程个数。
            numCourses -= 1
        # 若图中存在环，则一定有节点的入度不为 0。
        return numCourses == 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_canFinish(self) -> None:
        self.assertTrue(self.s.canFinish(2, [[1, 0]]))
        self.assertTrue(self.s.canFinish(3, [[1, 0], [2, 0]]))
        self.assertTrue(self.s.canFinish(4, [[3, 2], [2, 1], [1, 0]]))
        self.assertFalse(self.s.canFinish(2, [[1, 0], [0, 1]]))


if __name__ == "__main__":
    unittest.main()
