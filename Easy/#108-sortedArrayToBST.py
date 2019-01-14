"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 如果 nums 的长度等于 1，返回结果
        if len(nums) == 1: return TreeNode(nums[0])
        if len(nums) > 1:
            # root 取排在中间位置的数，不为整数的情况，则向下取整数
            mid = len(nums // 2)
            root = nums[mid]
            rootNode = TreeNode(root)
            # 对于二叉树的左边子根的处理，取 root 的前半部分的数，然后递归处理
            rootNode.left = self.sortedArrayToBST(nums[:mid])
            # 对于二叉树的右边子根的处理，取 root 的后半部分的数，然后递归处理
            rootNode.right = self.sortedArrayToBST(nums[mid+1:])
            return rootNode