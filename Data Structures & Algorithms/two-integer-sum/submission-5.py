class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}

        for idx, val in enumerate(nums):
            diff = target-val
            if diff in hmap:
                return [hmap[diff], idx]
            hmap[val] = idx
         