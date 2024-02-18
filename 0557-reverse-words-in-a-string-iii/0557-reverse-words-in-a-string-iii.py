class Solution:
    def reverseWords(self, s: str) -> str:            
        word_list = s.split()
        rev=""
        for i in word_list:
            word=""
            for j in i[::-1]:
                word+=j
            rev += word +" "
        return rev.strip()