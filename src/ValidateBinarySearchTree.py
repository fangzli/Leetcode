# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, min, max):
            print(min,max)
            if not node:
                return True
            if max is not None and node.val >= max:
                return False
            if min is not None and node.val <= min:
                return False
            return helper(node.left, min, node.val) and helper(node.right, node.val, max)

        return helper(root, None, None)

head =  TreeNode(0)
head.left = TreeNode(-1)
head.right = TreeNode(2)
M = Solution()
print(M.isValidBST(head))