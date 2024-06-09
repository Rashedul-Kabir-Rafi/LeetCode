class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        a = max(nums)
        b = min(nums)
        def compute_gcd(a,b):
            if  b == 0:
                return a
            else:
                return compute_gcd(b, a%b)
        return compute_gcd(a, b)