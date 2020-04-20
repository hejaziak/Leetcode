class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        rows = len(grid)
        if(rows > 0):
            cols = len(grid[0])
        else:
            cols = 0

        visited = [[False for i in range(cols)] for j in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1" and not visited[i][j]):
                    bfs(i, j, grid, visited)
                    count += 1

        return count


def bfs(i, j, grid, visited):

    if(not(i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))):
        return

    if(visited[i][j]):
        return
    else:
        visited[i][j] = True

    if(grid[i][j] == "1"):
        bfs(i+1, j, grid, visited)
        bfs(i, j+1, grid, visited)
        bfs(i-1, j, grid, visited)
        bfs(i, j-1, grid, visited)
    else:
        return
