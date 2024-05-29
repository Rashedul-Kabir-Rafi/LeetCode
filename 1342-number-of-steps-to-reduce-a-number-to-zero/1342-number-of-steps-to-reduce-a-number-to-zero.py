class Solution:
    def numberOfSteps(self, num: int) -> int:
        final = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                final += 1
            else:
                num -= 1
                final +=1 
        return final
                
        