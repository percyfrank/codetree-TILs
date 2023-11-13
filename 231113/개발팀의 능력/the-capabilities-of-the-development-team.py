from itertools import combinations

nums = list(map(int,input().split()))

total = sum(nums)
ans = float('inf')
for a,b in combinations(nums,2):
    sum1 = a+b
    tmp = []
    for num in nums:
        if num not in (a,b):
            tmp.append(num)
    for c,d in combinations(tmp,2):
        sum2 = c + d
        sum3 = total - sum1 - sum2
        if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
            continue
        MAX = max(sum1,sum2,sum3)
        MIN = min(sum1,sum2,sum3)
        ans = min(ans,MAX-MIN)

print(ans) if ans != float('inf') else print(-1)