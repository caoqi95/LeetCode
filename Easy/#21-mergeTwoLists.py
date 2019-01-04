"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# 参考：https://blog.csdn.net/u010636181/article/details/78260105
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = merge = ListNode(0)

        # 如果两个链表不为空，比较进行，并将小的那个赋给合并的链表头。
        # 小表头继续走一步，合并表头继续走一步。
        while l1 and l2:
            if l1.val < l2.val:
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next
            merge = merge.next

        # 注意：当由于其中一链表listNode1或者listNode2为null，导致跳出while循时，
        # 此时，还需要将另一不为null的链表的后续部分赋给合并链表。
        merge.next = l1 or l2

        return dummy.next

