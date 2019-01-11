"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# 也是使用递归的方法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return filpAndCheck(root.left, root.right)


# 1. 先确保两个根的值是否相等
# 2. 再确保一个根的两个子根是否与另一根的两个子根的翻转相同
def filpAndCheck(root1, root2):
    if root1 and root2:
        return root1.val == root2.val and filpAndCheck(root1.left, root2.right) and filpAndCheck(root1.right,
                                                                                                 root2.left)
    # 如果其中一个为 null，则返回 False
    # 如果两个都为 null，则返回 True
    return not (root1 or root2)