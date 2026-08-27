class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "":
            return ""
        
        hmapT = {}
        win = {}

        for i in t:
            hmapT[i] = 1 + hmapT.get(i, 0)
            
        have, need = 0, len(hmapT)
        res, resLen = [-1,-1], float("inf")
        l = 0 
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c,0)

            if c in hmapT and win[c] == hmapT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                win[s[l]] -= 1
                if s[l] in hmapT and win[s[l]] < hmapT[s[l]]:
                    have -= 1
                l += 1
        l, r = res 
        return s[l:r+1] if resLen != float("inf") else ""


            

