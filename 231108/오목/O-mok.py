import sys

maps = [list(map(int,input().split())) for _ in range(19)]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

for i in range(19):
    for j in range(19):
        if maps[i][j] == 0:
            continue

        for dx,dy in zip(dxs,dys):
            x,y = i,j
            cnt = 1
            while True:
                nx = x + dx
                ny = y + dy
                if not in_range(nx,ny) or maps[nx][ny] != maps[i][j]:
                    break
                cnt += 1
                x = nx
                y = ny

                if cnt == 5:
                    print(maps[i][j])
                    print(i+2*dx+1,j+2*dy+1)
                    sys.exit()

print(0)