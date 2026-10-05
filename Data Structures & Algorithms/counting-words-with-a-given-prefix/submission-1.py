class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        N = len(pref)
        count = 0 
        for w in words:
            if w[:N] == pref:
                count += 1
        return count 