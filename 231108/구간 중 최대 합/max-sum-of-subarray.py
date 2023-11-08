n,k = tuple(map(int,input().split()))
nums = list(map(int,input().split()))

ans = 0
for i in range(n-k+1):
    tmp = sum(nums[i:i+k])
    ans = max(ans,tmp)
print(ans)