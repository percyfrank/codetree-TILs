n,h,t = tuple(map(int,input().split()))
heights = list(map(int,input().split()))

ans = float('inf')
for i in range(n-t+1):
    cost = 0
    for j in range(i,i+t):
        if heights[j] != h:
            cost += abs(heights[j]-h)
    ans = min(ans,cost)

print(ans)