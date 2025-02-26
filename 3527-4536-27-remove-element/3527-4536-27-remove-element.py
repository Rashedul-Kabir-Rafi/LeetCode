class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in nums:
            if i != val:
                nums[n] = i
                n += 1
        return n