n,k = tuple(map(int,input().split()))

position = [0] * 101


def in_range(idx):
    return idx >=0 and idx < 101

for _ in range(n):
    candy, pos = tuple(map(int,input().split()))
    position[pos] += candy

ans = 0
for i in range(101):
    tmp = 0
    for j in range(i-k,i+k+1):
        if in_range(j):
            tmp += position[j]
    ans = max(ans,tmp)

print(ans)