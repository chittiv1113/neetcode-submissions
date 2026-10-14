from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if (not 0 <= row < len(grid) or 
                    not 0 <= col < len(grid[0]) or 
                    grid[row][col] != 1):
                        continue

                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1 
            time += 1
        
        if fresh != 0 :
            return -1
        else:
            return time
                

                

        