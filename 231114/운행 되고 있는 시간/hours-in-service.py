n = int(input())
works = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    cnt = [0] * 1001
    for j in range(n):
        if j == i:
            continue     
        start = works[j][0]
        end = works[j][1]
        for work in range(start,end):
            cnt[work] += 1

    tmp = 1001 - cnt.count(0)
    ans = max(ans,tmp)
    
print(ans)