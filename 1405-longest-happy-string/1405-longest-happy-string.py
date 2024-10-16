class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        
        while True:
            max_count = max(a, b, c)
            if max_count == 0:
                break
            
            if max_count == a:
                if len(result) >= 2 and result[-1] == result[-2] == 'a':
                    if b >= c and b > 0:
                        result.append('b')
                        b -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        break  
                else:
                    result.append('a')
                    a -= 1
            
            elif max_count == b:
                if len(result) >= 2 and result[-1] == result[-2] == 'b':
                    if a >= c and a > 0:
                        result.append('a')
                        a -= 1
                    elif c > 0:
                        result.append('c')
                        c -= 1
                    else:
                        break
                else:
                    result.append('b')
                    b -= 1
            
            else: 
                if len(result) >= 2 and result[-1] == result[-2] == 'c':
                    if a >= b and a > 0:
                        result.append('a')
                        a -= 1
                    elif b > 0:
                        result.append('b')
                        b -= 1
                    else:
                        break
                else:
                    result.append('c')
                    c -= 1
        
        return ''.join(result)
