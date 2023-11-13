n = int(input())

answers = []
for _ in range(n):
    answers.append(list(map(int,input().split())))

cnt = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or j == k or k == i:
                continue
            flag = True
            for num,cnt1,cnt2 in answers:
                num = str(num)
                a = int(num[0])
                b = int(num[1])
                c = int(num[2])
                tmp1,tmp2 = 0,0
                if i == a:
                    tmp1 += 1
                else:
                    if i in (b,c):
                        tmp2 += 1
                if j == b:
                    tmp1 += 1
                else:
                    if j in (a,c):
                        tmp2 += 1
                if k == c:
                    tmp1 += 1
                else:
                    if k in (a,b):
                        tmp2 += 1
                
                if tmp1 != cnt1 or tmp2 != cnt2:
                    flag = False
                    break
            
            if flag:
                cnt += 1

print(cnt)