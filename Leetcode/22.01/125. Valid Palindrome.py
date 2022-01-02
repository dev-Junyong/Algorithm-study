from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        dq = deque()
        
        for char in s:
            if char.isalnum():
                dq.append(char.lower())
            
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        
        return True
            