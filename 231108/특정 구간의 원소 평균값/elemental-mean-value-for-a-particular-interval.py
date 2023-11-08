n = int(input())
nums = list(map(int,input().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        tmp = 0
        for k in range(i,j+1):
            tmp += nums[k]
        if tmp == 0 or j == i-1:
            continue
        avg = tmp / (j-i+1)
        for l in range(i,j+1):
            if avg == nums[l]:
                cnt += 1
                break

print(cnt)