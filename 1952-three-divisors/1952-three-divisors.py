class Solution:
    def isThree(self, n: int) -> bool:
        sqrt_n = int(n**0.5)
        if (sqrt_n * sqrt_n) != n:
            return False
        if sqrt_n < 2:
            return False
        
        for i in range(2,int(sqrt_n**0.5) + 1):
            if sqrt_n % i == 0:
                return False
        return True
            