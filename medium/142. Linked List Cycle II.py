# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        fast = head
        slow = head

        if_ = 0
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                if_ = 1
                break

        if if_ == 0:
            return 
        else:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next

            return fast
        
