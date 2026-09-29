class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, col, visited) -> bool:
    
            if not (0 <= row < len(grid)):
                return False 
            if not (0 <= col < len(grid[0])):
                return False 
            
            if grid[row][col] == '0':
                return False
            if (row, col) in visited:
                return False 
            visited.add((row,col))

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dir_r, dir_c in directions:
                dfs(grid, row + dir_r, col + dir_c, visited)

            return True 
        
        visited = set()
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    if dfs(grid, row, col, visited):
                        count += 1 
        return count  