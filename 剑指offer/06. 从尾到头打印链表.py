# 递归法，栈法很简单

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        if head is None:
            return []
        
        return self.reversePrint(head.next) + [head.val]
