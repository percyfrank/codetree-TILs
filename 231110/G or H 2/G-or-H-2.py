from itertools import combinations

n = int(input())

# arr = [0] * 101
arr = dict()

for _ in range(n):
    pos,alpha = input().split()
    # arr[pos] += 1
    arr[int(pos)] = alpha

tmp = sorted(list(arr.keys()))

ans = 0
if n == 1:
    ans = 0
else:
    for start,end in combinations(tmp,2):
        if start > end:
            continue
        g_cnt = 0
        h_cnt = 0
        for pos in range(start,end+1):
            if pos in arr.keys():
                if arr[pos] == "G":
                    g_cnt += 1
                elif arr[pos] == "H":
                    h_cnt += 1
            if h_cnt == 0 or g_cnt == 0 or h_cnt == g_cnt:
                tmp = end-start
            ans = max(ans,tmp) 
    # for i in range(len(tmp)):
    #     for j in range(i+1,len(tmp)-1):
    #         g_cnt = 0
    #         h_cnt = 0
    #         for k in range(i,j+1):
    #             if arr[tmp[k]] == "G":
    #                 g_cnt += 1
    #             elif arr[tmp[k]] == "H":
    #                 h_cnt += 1
    #         if h_cnt == 0 or g_cnt == 0 or h_cnt == g_cnt:
    #             tmp = j-i
    #         ans = max(ans,tmp)

print(ans)