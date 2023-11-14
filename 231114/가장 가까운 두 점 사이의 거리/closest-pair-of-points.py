n = int(input())
coords = [list(map(int,input().split())) for _ in range(n)]

ans = float('inf')
for i in range(n):
    for j in range(i+1,n):
        tmp = (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2
        ans = min(ans,tmp)
    
print(ans)