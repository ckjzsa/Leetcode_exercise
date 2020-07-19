class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        stack = []
        root = float('+inf')

        for i in range(len(postorder)-1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            
            stack.append(postorder[i])
        
        return True
