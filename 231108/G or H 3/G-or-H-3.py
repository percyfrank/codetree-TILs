n,k = tuple(map(int,input().split()))

info = dict()
for _ in range(n):
    num,alpha = input().split()
    info[int(num)] = alpha   

arr = [0] * (max(info.keys())+1)
for key,value in info.items():
    arr[key] = 2 if value == "H" else 1

ans = 0
for i in range(1,len(arr)-k):
    tmp = 0
    for j in range(i,i+k+1):
        tmp += arr[j]
    ans = max(ans,tmp)

print(ans)