class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(i) + 32) if i.isupper() else i for i in s)