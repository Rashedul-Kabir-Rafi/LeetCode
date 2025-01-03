class Solution:
    def minTimeToType(self, word: str) -> int:
        a = ord('a') 
        count = 0
        for i in range(len(word)):
            b = ord(word[i])  
            if i == 0:
                min_position = min(abs(b - a), 26 - abs(b - a))  
            else:
                c = ord(word[i - 1])  
                min_position = min(abs(b - c), 26 - abs(b - c))  
            count += min_position + 1

        return count
