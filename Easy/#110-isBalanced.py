"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# solution from this site's comment:
#  https://leetcode.com/problems/balanced-binary-tree/discuss/35886/A-simple-Python-recursive-solution-172ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def __init__(self):
        self.d = {}

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(root):

            # 如果 root 为空
            if not root:
                return 0
            # 如果 root 存在 self.d 中，则返回该根的深度
            if (root in self.d): return self.d[root]
            # 计算根的深度，存储在 self.d 中
            self.d[root] = 1 + max(depth(root.left), depth(root.right))

            return self.d[root]

        if not root:
            return True

        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)



