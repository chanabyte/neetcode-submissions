class Solution:
    def isPalindrome(self, s: str) -> bool:
        ip = "".join(char.lower() for char in s if char.isalnum())
        start = 0
        end = len(ip)-1
        for i in range((len(ip) + 1) // 2):
            if(ip[start] != ip[end]): 
                print(ip[start], start,   ip[end], end)
                return False
            start+=1;
            end -= 1;

        return True 
