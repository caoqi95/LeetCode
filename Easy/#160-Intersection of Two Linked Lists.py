"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        lenA, lenB = 0, 0

        # 计算链表A的长度
        while curA is not None:
            lenA += 1
            curA = curA.next
        # 计算链表B的长度
        while curB is not None:
            lenB += 1
            curB = curB.next
        # 初始化为各自的链表头
        curA, curB = headA, headB
        # 如果A的长度长，从和B相同长度的位置开始
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        # 如果B的长度长，从和A相同长度的位置开始
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        
        # 如果两个链表不相同则继续
        while curB != curA:
            curB = curB.next
            curA = curA.next
        
        return curA