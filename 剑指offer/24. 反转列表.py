# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        new = ListNode(head.val)
        new.next = None
        head = head.next

        while head:
            temp = head.next
            head.next = new
            new = head
            head = temp

        return new


# 递归法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(last, cur):
            if cur is None: 
                return cur
            next = cur.next
            cur.next = last
            
            if next is None: 
                return cur
            
            return helper(cur, next)

        return helper(None, head)
