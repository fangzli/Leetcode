# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l3 = ListNode(0)
        isCarry = False
        while l1 and l2:
            dummy = ListNode(0)
            if isCarry == True:
                dummy.val += 1
            if l1.val + l2.val < 10:
                dummy.val = l1.val + l2.val
                isCarry = False
            elif l1.val + l2.val >= 10:
                dummy.val = l1.val + l2.val - 10
                isCarry = True

            l3 = dummy
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

Solution(object)
