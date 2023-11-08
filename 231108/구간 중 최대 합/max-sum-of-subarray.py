n,k = tuple(map(int,input().split()))
nums = list(map(int,input().split()))

ans = 0
for i in range(n-k+1):
    tmp = 0
    for j in range(i,i+k):
        tmp += nums[j]
    ans = max(ans,tmp)
print(ans)