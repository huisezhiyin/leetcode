class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(tin) == 1:
            return TreeNode(pre[0])
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return res
