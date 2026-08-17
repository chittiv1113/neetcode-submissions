class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i))+"#"+i)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            len_word = int(s[i:j])
            res.append(s[j+1:j+1+len_word])
            i = j+1+len_word
        return res
        

