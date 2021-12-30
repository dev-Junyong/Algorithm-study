class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        
        if numRows < 1:
            return answer
        
        for i in range(numRows):
            row = []
            if i == 0:
                row.append(1)
            else:
                row.insert(0, 1)
                row.insert(i, 1)
                for j in range(1, i):
                    left_top = answer[i - 1][j - 1]
                    right_top = answer[i - 1][j]
                    row.insert(j, left_top + right_top)
            answer.append(row)
        return answer