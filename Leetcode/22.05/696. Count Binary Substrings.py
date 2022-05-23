class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = []
        curr = 1
        for i in range(len(s)-1):
            if s[i] == s[i + 1]:
                curr += 1
            else:
                arr.append(curr)
                curr = 1
        if curr: 
            arr.append(curr)
        
        temp = []
        for j in range(len(arr)-1):
            temp.append(min(arr[j], arr[j + 1]))
        
        return sum(temp)
