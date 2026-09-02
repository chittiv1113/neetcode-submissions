class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l,r = 0, len(s)-1

        # while l<r:
        #     if s[l].lower() != s[r].lower():
        #         return False 
        #     else:
        #         l += 1
        #         r -= 1
        # return True 

        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()
        return string == string [::-1]