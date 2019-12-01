# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        value = []
        while head:
            value.append(head.val)
            head = head.next

        j = -1
        for i in range(len(value) // 2):
            if value[i] != value[j]:
                return False
            
            j = j - 1
        
        return True
    





