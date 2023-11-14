from itertools import combinations

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]


def get_area(x1,y1,x2,y2,x3,y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))

ans = 0
for (x1,y1),(x2,y2),(x3,y3) in combinations(points,3):
    if y1 == y2 == y3 or x1 == x2 == x3:
        continue
    if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
        ans = max(ans,get_area(x1,y1,x2,y2,x3,y3))
    
print(ans)