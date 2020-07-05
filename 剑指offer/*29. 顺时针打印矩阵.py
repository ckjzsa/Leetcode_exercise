class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        left, right = 0, len(matrix[0])  # column
        top, bottom = 0, len(matrix)  # row
        res = []

        while True:
            for i in range(left, right):
                res.append(matrix[top][i])    
            top += 1
            if top >= bottom:
                break
            
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if right <= left:
                break

            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            if bottom <= top:
                break
            
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left >= right:
                break
        
        return res


            
