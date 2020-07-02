# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        if head.val == val:
            return head.next

        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                break

            head = head.next
        
        return temp
