class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        word = "".join(set(word))
        for i in word:
            if i.isupper():
                if i.lower() in word:
                    count += 1
        return count