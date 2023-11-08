n,k = tuple(map(int,input().split()))

arr = [0] * 10001
for _ in range(n):
    num, alpha = input().split()
    arr[int(num)] = 2 if alpha == "H" else 1

ans = 0
for i in range(1,len(arr)-k):
    tmp = 0
    for j in range(i,i+k+1):
        tmp += arr[j]
    ans = max(ans,tmp)

print(ans)