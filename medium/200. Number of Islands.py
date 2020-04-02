class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        # 左右扩充
        for row in grid:
            row.insert(0, 0)
            row.append(0)
        
        # 上下扩充
        row_0 = [0 for _ in range(len(grid[0]))]
        grid.insert(0, row_0)
        grid.append(row_0)

        def reset(i, j):
            if grid[i][j] == '1':
                grid[i][j] = 0
                reset(i-1, j)
                reset(i+1, j)
                reset(i, j+1)
                reset(i, j-1)
        
        count = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == '1':
                    count += 1
                reset(i, j)
        
        return count


