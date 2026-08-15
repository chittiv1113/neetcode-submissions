class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hmap = {}
        for ch in s:
            if ch not in s_hmap:
                s_hmap[ch] = 1
            else:
                s_hmap[ch] += 1
        
        t_hmap = {}
        for ch in t:
            if ch not in t_hmap:
                t_hmap[ch] = 1
            else:
                t_hmap[ch] += 1   

        if s_hmap == t_hmap:
            return True 
        else:
            return False
             