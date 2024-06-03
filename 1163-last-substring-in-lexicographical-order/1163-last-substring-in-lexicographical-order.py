class Solution:
    def lastSubstring(self, s: str) -> str:
        max_substring = ""
        for i in range(len(s)):
            substring = s[i:]
            if substring > max_substring:
                max_substring = substring
        return max_substring
