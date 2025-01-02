class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list(set(nums))
        max = 0
        max_digit = 0
        for i in range(len(unique)):
            a = nums.count(unique[i])
            if a > max:
                max = a
                max_digit = unique[i]
        return max_digit


                