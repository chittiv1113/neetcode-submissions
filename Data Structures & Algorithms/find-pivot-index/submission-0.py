class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)
        
        for i in range(1,len(prefix)):
            if prefix[-1] - prefix[i] == prefix[i-1]:
                return i-1
        return -1 