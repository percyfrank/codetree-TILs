n = int(input())
a1,b1,c1 = tuple(map(int,input().split()))
a2,b2,c2 = tuple(map(int,input().split()))

result = set()
cnt = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            if (abs(a-a1) <= 2 or abs(a-a1) >= n-2) and (abs(b-b1) <= 2 or abs(b-b1) >= n-2) and (abs(c-c1) <= 2 or abs(c-c1) >= n-2):
                result.add((a,b,c))
            if (abs(a-a2) <= 2 or abs(a-a2) >= n-2) and (abs(b-b2) <= 2 or abs(b-b2) >= n-2) and (abs(c-c2) <= 2 or abs(c-c2) >= n-2):
                result.add((a,b,c))
    
print(len(result))