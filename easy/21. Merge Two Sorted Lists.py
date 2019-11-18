# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        dummy = ListNode(-1)

        new_head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                new_head.next = l1
                l1 = l1.next
                
            else:
                new_head.next = l2
                l2 = l2.next
            
            new_head = new_head.next

        if l1 == None:
            new_head.next = l2
        else:
            new_head.next = l1
        
        return dummy.next
