class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # pass 1: find k, the real index of the minimum
        l, r = -1, n
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid
        k = r

        # plain binary search on an inclusive range
        def bsearch(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        # pass 2: pick the run that could contain target, then search it
        if nums[k] <= target <= nums[-1]:
            return bsearch(k, n - 1)
        else:
            return bsearch(0, k - 1)