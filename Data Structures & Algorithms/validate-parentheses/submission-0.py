class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ")" : "(",
            "}" : "{",
            "]" : "[" 
        }
        stack = []
        for i in s:
            if i in hmap and stack and hmap[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True 