import copy

n,m = tuple(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

b_dict = dict()
for num in b:
    b_dict.setdefault(num,0)
    b_dict[num] += 1
# print(b_dict)

cnt = 0
for i in range(n-m+1):
    tmp = copy.deepcopy(b_dict)
    for j in range(i,i+m):
        if a[j] in tmp.keys():
            tmp[a[j]] -= 1
        else:
            break

    flag = True
    for value in tmp.values():
        if value != 0:
            flag = False
            break

    if flag:
        cnt += 1
print(cnt)