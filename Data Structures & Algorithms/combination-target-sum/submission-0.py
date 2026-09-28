class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(start,path):
            if sum(path) > target:
                return 
            if sum(path) == target:
                return res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i,path)
                path.pop()

        backtrack(0,[])
        return res 