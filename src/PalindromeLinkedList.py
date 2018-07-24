# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(2)


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Method 1: This method use O(n) space
        # stack = []
        # while head:
        #       stack.append(head.val)
        #       head = head.next
        # return stack == stack[::-1]
        if not head:
            return True
        # Find Midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Now prev is the new head for second half
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True


M = Solution()
print(M.isPalindrome(test))


