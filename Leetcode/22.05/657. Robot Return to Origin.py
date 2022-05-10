class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i = 0
        j = 0
        for move in moves:
            if move == 'L':
                j -= 1
            elif move == 'R':
                j += 1
            elif move == 'U':
                i -= 1
            elif move == 'D':
                i += 1

        if i == 0 and j == 0:
            return True
        return False