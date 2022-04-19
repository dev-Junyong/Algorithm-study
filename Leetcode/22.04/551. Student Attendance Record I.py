class Solution:
    def checkRecord(self, s: str) -> bool:
        chk = Counter(s)
        if chk['A'] <= 1:
            if 'LLL' not in s:
                return True
            else:
                return False
        else:
            return False