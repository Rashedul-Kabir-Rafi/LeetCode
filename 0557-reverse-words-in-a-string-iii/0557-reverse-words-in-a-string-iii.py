class Solution:
    def reverseWords(self, s: str) -> str:            
        word_list = s.split()
        rev= ("".join(reversed(word)) for word in word_list)
        return " ".join(rev)