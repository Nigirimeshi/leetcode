# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def show(self):
        return

    def construct(self, li=None):
        if not li:
            return None
        tl = []
        for i in li:
            if i is None:
                tl.append(None)
            else:
                tl.append(TreeNode(i))
        for idx in range(len(li) // 2):
            if idx * 2 + 1 < len(tl) and tl[idx * 2 + 1]:
                tl[idx].left = tl[idx * 2 + 1]

            if idx * 2 + 2 < len(tl) and tl[idx * 2 + 2]:
                tl[idx].right = tl[idx * 2 + 2]
        self.root = tl[0]

    def pre_order(self, cur):
        if not cur:
            return
        print(cur.val)
        self.pre_order(cur.left)
        self.pre_order(cur.right)

    def in_order(self, cur):
        if not cur:
            return
        self.in_order(cur.left)
        print(cur.val)
        self.in_order(cur.right)

    def post_order(self, cur):
        if not cur:
            return
        self.post_order(cur.left)
        self.post_order(cur.right)
        print(cur.val)

    @staticmethod
    def level_order(cur):
        dq = deque()
        dq.append(cur)
        while dq:
            tmp = dq.popleft()
            if not tmp:
                continue
            print(tmp.val)
            dq.append(tmp.left)
            dq.append(tmp.right)
