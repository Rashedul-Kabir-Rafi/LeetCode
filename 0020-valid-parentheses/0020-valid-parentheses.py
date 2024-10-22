class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (i == ')' and top != '(') or (i == '}' and top != '{') or (i == ']' and top != '[') :
                    return False
        return not stack