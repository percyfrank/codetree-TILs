from itertools import combinations

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = -1
for a,b,c in combinations(nums,3):
    max_len = max(len(str(a)),len(str(b)),len(str(c)))
    tmp_a = "0"*(max_len-len(str(a)))+str(a)
    tmp_b = "0"*(max_len-len(str(b)))+str(b)
    tmp_c = "0"*(max_len-len(str(c)))+str(c)
    
    flag = True
    for i in range(max_len):
        if int(tmp_a[i]) + int(tmp_b[i]) + int(tmp_c[i]) >= 10:
            flag = False
            break
    if flag:
        ans = max(ans,a+b+c)
        
print(ans)