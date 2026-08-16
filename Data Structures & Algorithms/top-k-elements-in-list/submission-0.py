class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else: 
                hmap[i] += 1
        print(max(hmap.values()))
        result = []
        for _ in range(k):
            max_key = max(hmap, key=hmap.get)
            result.append(max_key)
            hmap.pop(max_key) 
        return result


        