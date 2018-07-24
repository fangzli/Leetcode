# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Method 1: Recursive
        if root is None:
            return True
        else:
            return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return (left.val == right.val) and self.helper(left.left, right.right) and self.helper(left.right,
                                                                                                   right.left)
