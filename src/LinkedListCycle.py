# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def cycleLength(head):
        slow = fast = head
        slowct = fastct = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            slowct += 1
            fastct += 2
            if slow == fast:
                return fastct - slowct
        return 0


test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(2)
test.next.next.next.next = test.next


print Solution.cycleLength(test)