n = int(input())
nums = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(i+2,n):
        tmp = nums[i] + nums[j]
        ans = max(ans,tmp)
print(ans)