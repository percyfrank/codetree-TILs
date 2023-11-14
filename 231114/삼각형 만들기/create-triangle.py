from itertools import combinations

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]


def get_area(x1,y1,x2,y2,x3,y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) // 2

ans = 0
for (x1,y1),(x2,y2),(x3,y3) in combinations(points,3):
    if y1 == y2 == y3 or x1 == x2 == x3:
        continue
    elif y1 == y2:
        if x3 == x1 or x3 == x2:
            ans = max(ans,get_area(x1,y1,x2,y2,x3,y3))
    elif y2 == y3:
        if x1 == x2 or x1 == x3:
            ans = max(ans,get_area(x1,y1,x2,y2,x3,y3))
    elif y1 == y3:
        if x2 == x1 or x2 == x3:
            ans = max(ans,get_area(x1,y1,x2,y2,x3,y3))
    
print(ans*2)