class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]
        
    def binary_search(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            middle = (left+right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                index = middle
                if leftBias:
                    right = middle - 1
                else:
                    left = middle + 1
        return index