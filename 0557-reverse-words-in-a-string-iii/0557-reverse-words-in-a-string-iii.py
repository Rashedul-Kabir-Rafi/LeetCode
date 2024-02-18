class Solution:
    def reverseWords(self, s: str) -> str:            
        a =  (''.join(reversed(word)) for word in s.split())
        return ' '.join(a)