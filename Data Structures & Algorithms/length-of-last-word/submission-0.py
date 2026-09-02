class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []

        for i in s:
            stack.append(i)
        
        while stack and stack[-1] == " ":
            stack.pop()
        
        counter = 0
        while stack and stack[-1] != " ":
            stack.pop()
            counter += 1

        return counter 