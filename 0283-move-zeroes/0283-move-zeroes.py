class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_z = nums.count(0)
        new_list = [x for x in nums if x != 0] 
        z_list = [0] * count_z
        new_list.extend(z_list)
        nums[:] = new_list
