# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        n = 1
        while n < k:
            n += 1
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        return slow
        

