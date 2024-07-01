class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            if (i+1)%3 == 0 or (i-1)%3 ==0:
                total += 1
        return total