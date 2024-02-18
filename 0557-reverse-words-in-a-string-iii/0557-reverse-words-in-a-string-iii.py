class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = (''.join(reversed(word)) for word in words)
        return ' '.join(reversed_words)