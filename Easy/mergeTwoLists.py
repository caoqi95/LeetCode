# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    dummy = cur = ListNode(0)

    while l1 and l2 :
        if l1.val < l2.val:
            cur, l1 = l1, l1.next
        else:
            cur, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2

    return dummy.next

if __name__ == "__main__":
    l1 = ListNode([1,2,3])
    l2 = ListNode([1,3,4])
    mergeTwoLists(l1, l2)