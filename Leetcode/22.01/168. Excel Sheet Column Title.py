class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber != 0:
            temp = chr(ord('A') + (columnNumber-1) % 26)
            columnNumber = (columnNumber-1) // 26
            res = temp + res
        return res
        