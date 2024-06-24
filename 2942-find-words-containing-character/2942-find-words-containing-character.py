class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final_array = []
        for i in range(len(words)):
            if x in words[i]:
                final_array.append(i)
        return final_array