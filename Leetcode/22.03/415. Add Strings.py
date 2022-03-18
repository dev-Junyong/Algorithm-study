class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self._int(num1) + self._int(num2))

    def _int(self, num):
        res = 0
        cnt = 1
        for i in num[::-1]:
            res += cnt * (ord(i) - ord('0'))
            cnt *= 10
        return res