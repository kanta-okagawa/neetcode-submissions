class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''
        for i in s:
            if isalnum(i):
                text += i
        return text == text[::-1]