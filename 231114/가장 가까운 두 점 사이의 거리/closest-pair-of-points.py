n = int(input())
coords = [list(map(int,input().split())) for _ in range(n)]

def dist(i,j):
    return (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2

ans = float('inf')
for i in range(n):
    for j in range(i+1,n):
        ans = min(ans,dist(i,j))
    
print(ans)