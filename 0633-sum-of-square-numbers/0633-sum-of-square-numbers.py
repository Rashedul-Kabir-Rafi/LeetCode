import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False #negative numbers can't be the sum of real numbers square
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            sum_squares = a**2 + b**2
            if sum_squares  == c:
                return True
            elif sum_squares < c:
                a += 1
            else:
                b -= 1
        return False
            
    