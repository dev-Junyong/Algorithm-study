class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        s = 0
        e = len(currentState) - 1
        while s < e:
            if currentState[s] == '+':
                while s < e and currentState[s + 1] == '+':
                    res.append(currentState[:s] + '--' + currentState[s + 2:])
                    s += 1
            s += 1
        return res