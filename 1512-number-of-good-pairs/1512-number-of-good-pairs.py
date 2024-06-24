class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        pairs = {}
        for i in nums:
            if i not in pairs:
                pairs[i] = 1
            else:
                good_pairs += pairs[i]
                pairs[i] += 1                  
        return good_pairs
    
