class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs
                