class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0 
        for i in range(k):
            if blocks[i] == "W":
                w_count += 1
        
        res = w_count
        l = 0 
        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                w_count += 1
            if blocks[l] == 'W':
                w_count -= 1
            l += 1
            res = min(res, w_count)
        return res
                
            

