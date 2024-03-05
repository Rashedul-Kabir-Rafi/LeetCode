class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new =[]
        for i in nums1:
            if i in nums2:
                    new.append(i)
        new = list(set(new))
        return new