class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pac, atl = set() , set()

        def dfs(r,c,visited,prevheight):
            if not (0 <= r < row):
                return 
            if not (0 <= c < col):
                return 
            if heights[r][c] < prevheight:
                return 
            if (r,c) in visited:
                return 
            visited.add((r,c)) 

            directions = [[0,1],[0,-1],[-1, 0],[1,0]]
            for dir_r, dir_c in directions:
                dfs(r+dir_r, c+dir_c,visited, heights[r][c])


        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col - 1,atl,heights[r][col -1])
        
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        res = []
        tmp = pac.intersection(atl)
        for i in tmp:
            res.append(list(i))
        return res

            
