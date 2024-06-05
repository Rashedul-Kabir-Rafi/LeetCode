class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_element = list(set(nums))
        return len(nums) != len(unique_element)