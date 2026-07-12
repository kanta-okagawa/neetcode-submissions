class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''
        for i in range(len(s)):
            if isalnum(s[i]):
                text += i
        return text == text[::-1]