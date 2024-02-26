class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second= "asdfghjkl"
        third= "zxcvbnm"
        rows = [first, second, third]
        result = []
        for word in words:
            for row in rows:
                if all(letter.lower() in row for letter in word.lower()):
                    result.append(word)
                    break
        return result
