class Solution:
    def isPalindrome(self, s: str) -> bool:
        ip = "".join(char.lower() for char in s if char.isalnum())

        return ip == ip[::-1]
