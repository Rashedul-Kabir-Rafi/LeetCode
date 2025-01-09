class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        outpt = []
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                outpt.append(i)
        return outpt