class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        grid = matrix
        row = len(grid)
        cols = len(grid[0])
        l,r = 0, row*cols-1

        while l<=r:
            mid = (r+l)//2
            val = grid[mid // cols][mid % cols]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True 
        return False  
        