"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 利用快慢指针证明一个链表是否为循环
        # 快指针的速度为 2N，慢指针的速度为 N

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 如果快指针赶上了慢指针
            if slow is fast:
                return True

        return False
