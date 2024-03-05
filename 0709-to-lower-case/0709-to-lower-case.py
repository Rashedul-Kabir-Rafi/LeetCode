class Solution:
    def toLowerCase(self, s: str) -> str:
        new = ''
        for i in s:
            i = chr(ord(i) + 32) if i.isupper() else i
            new+=i
        return new