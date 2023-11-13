from itertools import combinations

abilities = list(map(int,input().split()))

total = sum(abilities)
ans = float('inf')
for a,b,c in combinations(abilities,3):
    tmp = a + b + c
    rest = total - tmp
    ans = min(ans,abs(tmp-rest))
print(ans)