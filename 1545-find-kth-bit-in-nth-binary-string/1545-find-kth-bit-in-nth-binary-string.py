class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findBit( n, k):
            if n == 1:
                return '0'
            
            length = (1 << n) - 1
            mid = length // 2 + 1
            
            if k == mid:
                return "1"
            elif k < mid:
                return findBit(n-1, k)
            else:
                mirror_k = length - k +1
                return "1" if findBit(n-1, mirror_k) == '0' else '0'
            
        return findBit(n, k)
            
            
