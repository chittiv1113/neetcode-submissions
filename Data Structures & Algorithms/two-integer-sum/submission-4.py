class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # s, f = 0, 1
        # while f<len(nums):
        #     if nums[s] + nums[f] == target:
        #         return True 
        #     s += 1 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]