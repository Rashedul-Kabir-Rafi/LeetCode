class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda i: nums[nums[i]], range(len(nums))))