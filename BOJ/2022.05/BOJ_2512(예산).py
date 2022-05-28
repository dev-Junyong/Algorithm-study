
n = int(input())
budg = list(map(int, input().split()))
m = int(input())

low = 0
high = max(budg)
mid = (low + high) // 2
res = 0

def check(mid):
    total = 0
    for i in budg:
        total += min(i, mid)
    return total <= m

while low <= high:
    if check(mid):
        low = mid + 1
        res = mid
    else:
        high = mid - 1 
    
    mid = (low + high) // 2


print(res)
