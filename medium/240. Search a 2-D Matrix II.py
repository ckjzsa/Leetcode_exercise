class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = len(matrix) - 1
        col = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                row = i
                break
            elif matrix[i][0] == target:
                return True
        
        for j in range(len(matrix[0])):
            if matrix[0][j] > target:
                col = j
                break
            elif matrix[0][j] == target:
                return True

        
        for i in range(row+1):
            for j in range(col+1):
                if matrix[i][j] == target:
                    return True

        return False
