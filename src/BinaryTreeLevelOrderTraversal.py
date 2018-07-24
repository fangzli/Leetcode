# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        levels = []
        level = [root]
        while level:
            levels.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return levels

class Solution2(object):
    def levelOrder(self, root):
        out = []
        def helper(level, root):
            if root != None:
                if level == len(out :
                    out.append([]
                out[level].append(root.val)
                helper(level + 1, root.left)
                helper(level + 1, root.right)
        helper(0, root)
        return out