class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        max_area = 0 
        l, r = 0, len(nums)-1
        while l<r:
            base = r-l 
            if nums[l] > nums[r]:
                height = nums[r]
                area = base*height 
                r -= 1
            elif nums[l] <= nums[r]:
                height = nums[l]
                area = base*height 
                l += 1

            max_area = max(max_area, area)
        return max_area

        