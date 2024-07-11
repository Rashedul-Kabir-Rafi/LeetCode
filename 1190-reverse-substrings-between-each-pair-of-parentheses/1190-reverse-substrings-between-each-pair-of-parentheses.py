class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)  
        l = len(s)
        
        while '(' in s:
            a = 0
            b = 0
            for i in range(l):
                if s[i] == "(":
                    a = i
                elif s[i] == ")":
                    b = i
                    s[a+1:b] = s[a+1:b][::-1]
                    s.pop(b)
                    s.pop(a)
                    break  
            l = len(s)  
        return ''.join(s)