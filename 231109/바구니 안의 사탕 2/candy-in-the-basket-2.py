n,k = tuple(map(int,input().split()))

position = [0] * 101

for _ in range(n):
    candy, pos = tuple(map(int,input().split()))
    position[pos] += candy


ans = 0
for i in range(k,101-k):
    tmp = 0
    for j in range(i-k,i+k+1):
        tmp += position[j]
    # print(tmp)
    ans = max(ans,tmp)
print(ans)