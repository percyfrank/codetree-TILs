n = int(input())
coords = [list(map(int,input().split())) for _ in range(n)]

ans = float('inf')
for i in range(n):
    x,y = [],[]    
    for j in range(n):
        if j == i:
            continue
        x.append(coords[j][0])
        y.append(coords[j][1])
    area = (max(x)-min(x))*(max(y)-min(y))
    ans = min(ans,area)
print(ans)