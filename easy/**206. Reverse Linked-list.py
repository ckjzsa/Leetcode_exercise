# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        new_head = None
        
        while head:     
            tmp = head.next      # 备份原来head节点的next地址
            head.next = new_head  # head倒序进行
            new_head = head  # new_head正序进行
            head = tmp
        
        return new_head
