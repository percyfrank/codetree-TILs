n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]


max_cnt = 0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i == k and abs(j-l) <= 2:
                    continue
                max_cnt = max(max_cnt, grid[i][j] + grid[i][j+1] + grid[i][j+2]
                                     + grid[k][l] + grid[k][l+1] + grid[k][l+2])

print(max_cnt)