class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_pal(l,r):
            while l<r:
                if s[l]!= s[r]:
                    return False
                l += 1
                r -= 1
            return True 
             

        l, r = 0, len(s)-1
        counter = 0 
        while l<r:
            if s[l] != s[r]:
                if is_pal(l+1,r) or is_pal(l, r-1):
                    return True
                else:
                    return False  
            l += 1
            r -= 1
        return True 