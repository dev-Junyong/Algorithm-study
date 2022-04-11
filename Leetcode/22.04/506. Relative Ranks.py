class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)
        dict_rank = {}
        res = []
        for i in range(len(ranks)):
            dict_rank[ranks[i]] = i
        
        for s in score:
            rank = dict_rank[s]
            if rank == 0:
                res.append("Gold Medal")
            elif rank == 1:
                res.append("Silver Medal")
            elif rank == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(rank+1))
        return res