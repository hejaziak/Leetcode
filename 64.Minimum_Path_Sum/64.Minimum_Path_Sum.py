class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = (len(grid), len(grid[0]))
        print(rows)
        print(cols)

        mem = [[0 for i in range(cols)] for j in range(rows)]
        print(mem)

        mem[0][0] = grid[0][0]

        for i in range(1, rows):
            mem[i][0] = mem[i-1][0] + grid[i][0]

        for i in range(1, cols):
            mem[0][i] = mem[0][i-1] + grid[0][i]

        for i in range(1, rows):
            for j in range(1, cols):
                mem[i][j] = min(mem[i-1][j]+grid[i][j], (mem[i][j-1]+grid[i][j]))
                                
        return mem[rows-1][cols-1]
