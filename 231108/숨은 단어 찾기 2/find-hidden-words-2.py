n,m = tuple(map(int,input().split()))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

words = [list(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if words[i][j] == "L":            
            for dx,dy in zip(dxs,dys):
                nx1,ny1 = i + dx, j + dy    
                nx2,ny2 = i + dx * 2, j + dy * 2
                if in_range(nx1,ny1) and in_range(nx2,ny2) and words[nx1][ny1] == "E" and words[nx2][ny2] == "E":
                    cnt += 1

print(cnt)