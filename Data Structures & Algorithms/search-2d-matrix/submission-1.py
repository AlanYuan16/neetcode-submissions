class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # row
        n = len(matrix[0]) # column

        l = 0
        r = (m * n) - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // n # first itertation would be 5/4 = 1
            col = mid % n # this would be 5%4 and that would = 1

            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val > target:
                r = mid - 1 # let say it is 1,0 and we need to move it to 0,3
            else:
                l = mid + 1

        return False