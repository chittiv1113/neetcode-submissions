class Solution:
    def firstUniqChar(self, s: str) -> int:

        hmap = {}

        for i in s:
            if i not in hmap:
                hmap[i] = 1
            else: hmap[i] += 1

        for i in range(len(s)):
            if  hmap[s[i]] == 1:
                return i 
        return -1