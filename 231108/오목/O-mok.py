maps = [list(map(int,input().split())) for _ in range(19)]

ans,x,y = 0,0,0
for i in range(2,17):
    for j in range(2,17):
        if maps[i][j] != 0:
            if maps[i][j-2] == maps[i][j-1] == maps[i][j] == maps[i][j+1] == maps[i][j+2]:
                ans,x,y = maps[i][j],i+1,j+1
            elif maps[i-2][j] == maps[i-1][j] == maps[i][j] == maps[i+1][j] == maps[i+2][j]:
                ans,x,y = maps[i][j],i+1,j+1
            elif maps[i-2][j-2] == maps[i-1][j-1] == maps[i][j] == maps[i+1][j+1] == maps[i+2][j+2]:
                ans,x,y = maps[i][j],i+1,j+1
            elif maps[i-2][j+2] == maps[i-1][j+1] == maps[i][j] == maps[i+1][j-1] == maps[i+2][j-2]:
                ans,x,y = maps[i][j],i+1,j+1
        

if ans != 0:
    print(ans)
    print(x,y)
else:
    print(ans)