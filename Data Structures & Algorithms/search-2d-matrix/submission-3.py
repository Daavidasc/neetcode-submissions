class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        filas = len(matrix)
        columnas = len(matrix[-1])
        r = filas * columnas

        while l <= r:
            mid = (r + l) //2
            
            if mid//columnas >= filas or mid% columnas>columnas:
                return False

            if matrix[mid//columnas][mid%columnas] == target:
                return True

            if target > matrix[mid//columnas][mid%columnas]:
                l = mid + 1
            else:
                r = mid - 1

        return False