class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            s = [[1], [1, 1]]
            for row in range(3, numRows + 1):
                app = [1 for _ in range(row)]
                # 需要变化的为 app[1]-app[numRows - 2]
                for i in range(1, row - 1):
                    app[i] = s[row-2][i-1] + s[row-2][i]
                s.append(app)
            return s

        
