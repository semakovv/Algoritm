lst = [3, 3, 3, 1, 1, 0]
ln = len(lst)
print(ln)
cnt = 0
for i in range(ln - 1, -1, -1):
    print(lst[i])
    for j in range(i - 1, -1, -1):
        print(lst[i], lst[j])
        if lst[i] == lst[j]:
            cnt += 1
print(cnt)
