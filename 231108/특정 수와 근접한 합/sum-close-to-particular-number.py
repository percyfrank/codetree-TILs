n,s = tuple(map(int,input().split()))
nums = list(map(int,input().split()))

total = sum(nums)
ans = float('inf')

for i in range(n):
    for j in range(i+1,n):
        tmp = total - nums[i] - nums[j]
        ans = min(ans,abs(tmp-s))
        
print(ans)