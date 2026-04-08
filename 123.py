s = "1 2 3 4 5"
A = set(s)
print(A)
for i in A:
    cnt = 0
    for j in s:
        if i is j:
            cnt += 1
    if cnt >= 2:
        print(i, cnt, "YES")
    else:
        print(i, cnt, "NO")