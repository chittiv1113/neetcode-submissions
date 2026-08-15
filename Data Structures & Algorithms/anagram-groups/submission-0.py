class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in hmap: 
                hmap[sort] = [i]
            else:
                hmap[sort].append(i)
        
        output = [v for v in hmap.values()]
        return output