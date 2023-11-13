from itertools import combinations

nums = list(map(int,input().split()))

ans = float('inf')
tot = sum(nums)
for a,b in combinations(nums,2):
    tmp = []
    for num in nums:
        if num not in (a,b):
            tmp.append(num)
    for c,d in combinations(tmp,2):
        MAX = max(a+b,c+d,tot-(a+b+c+d))
        MIN = min(a+b,c+d,tot-(a+b+c+d))
        ans = min(ans,MAX-MIN)
print(ans)