class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sp = 0 

        for i in t:
            if sp >= len(s):
                return sp == len(s)
            if i == s[sp]:
                sp += 1
        return sp == len(s)
        


        
