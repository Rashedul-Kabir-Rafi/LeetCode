class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        length = len(grid)
        result = [[0] * (length - 2) for _ in range(length - 2)] 
        for i in range(length - 2):
            for j in range(length - 2):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        result[i][j] = max(result[i][j], grid[k][l])
        return result