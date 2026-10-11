class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w,b = 0,0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
            if blocks[i] == 'B':
                b += 1
        res = float('inf')
        total = k-b                   
        if total <= w:
            res = min(res,total)
        l = 0 
        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                w += 1
            if blocks[r] == 'B':
                b += 1
            if blocks[l] == "W":
                w -= 1
            if blocks[l] == "B":
                b -= 1
            l += 1
            total = k-b
            if total <= w:
                res = min(res,total)
        return res 

