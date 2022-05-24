import heapq
def solution(jobs):
    answer = 0
    jobs_len = len(jobs)
    t, et = 0, -1
    qu = []
    
    cnt = 0
    
    while cnt < jobs_len:
        for job in jobs:
            if et < job[0] <= t:
                answer += t - job[0]
                heapq.heappush(qu, job[1])
        if len(qu) > 0:
            answer += qu[0] * len(qu)
            et = t
            t += heapq.heappop(qu)
            cnt += 1
        else:
            t += 1
    res = answer // jobs_len        
    
    return res