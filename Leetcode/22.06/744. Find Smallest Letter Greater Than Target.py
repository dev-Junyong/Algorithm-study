class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = 0
        e = len(letters) - 1
        
        while s <= e:
            mid = (s + e) // 2
            
            if letters[mid] <= target:
                s = mid + 1
            else:
                e = mid - 1
        res = s % len(letters)
        
        return letters[res]