class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True 
            
            row_inbounds = r < len(board) and r >= 0
            col_inbounds = c < len(board[0]) and c >= 0 
            if not row_inbounds or not col_inbounds:
                return False 

            if word[i] != board[r][c]:
                return False 
            
            if (r,c) in path:
                return False 
            
            path.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dir_r,dir_c in directions:
                if dfs(r+dir_r,c+dir_c,i+1):
                    return True 
            path.remove((r,c))
            return False 
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,0):
                    return True
        return False 
            


