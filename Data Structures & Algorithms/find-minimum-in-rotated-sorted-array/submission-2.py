class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def is_before(mid):
            return nums[mid] > nums[-1]
         
        l,r = -1, len(nums)-1
        while r-l>1:
            mid = (r+l) // 2
            if is_before(mid):
                l = mid 
            else:
                r = mid 
        return nums[r] 