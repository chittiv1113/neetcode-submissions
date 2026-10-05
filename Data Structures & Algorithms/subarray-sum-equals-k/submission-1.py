class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0 
        hmap = { 0: 1}

        for i in nums:
            curSum += i 
            diff = curSum-k

            if diff in hmap:
                res += hmap[diff]

            if curSum not in hmap:
                hmap[curSum] = 1
            else:
                hmap[curSum] += 1

        return res

