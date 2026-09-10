class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False 

class wordDict:
    def __init__(self):
        self.root = TreeNode()

    def addword(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words:
            return []

        trie = wordDict()
        for i in words:
            trie.addword(i)

        def explore(r,c,node):
            row_inbounds = r >= 0 and r < len(board)
            col_inbounds = c >= 0 and c < len(board[0])
            if not row_inbounds or not col_inbounds:
                return False 

            if board[r][c] not in node.children:
                return False 
            if (r,c) in visited:
                return False
            visited.add((r,c))

            node = node.children[board[r][c]]
            if node.word:
                res.add(node.word)

            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dir_r, dir_c in directions:
                explore(r+dir_r, c+dir_c, node)
                
            visited.remove((r,c))

        res = set() #when root.word = True and 
        visited = set() #nodes visited 
        for row in range(len(board)):
            for col in range(len(board[0])):
                explore(row,col,trie.root)

        return list(res)
                     
        
        

        
                

                


                





















        