class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha = headA
        hb = headB
        while ha != hb:
            if ha:
                ha = ha.next
            else:
                ha = headB

            if hb:
                hb = hb.next
            else:
                hb = headA

        return hb
