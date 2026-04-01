# 1
# lst = [0, 1]
# sm = 0
# n = 0
# def func_for(lst1, sm1):
#     for i in lst1:
#         sm1 += i
#     return sm1
# print(func_for(lst, sm))
# def func_while(lst2, sm2, n2):
#     while n2 != len(lst2):
#         sm2 += lst2[n2]
#         n2 += 1
#     return sm2
# print(func_while(lst, sm, n))
# def func_return(lst3, sm3, n3):
#     if n3 != len(lst3):
#         sm3 += lst3[n3]
#         n3 += 1
#         return func_return(lst3, sm3, n3)
#     else:
#         return sm3
# print(func_while(lst, sm, n))
# 2
import random
# lst = [random.choise(-9, 9) for i in random.range(0,10)]
lst = [3, 2, 1, 0]
def sort(LST):
    swap = False
    n = 0
    for i in LST:
        if i > i[n+1]:
            i, i[n+1] = i[n+1], i
            n += 1
            swap = True
    if swap:
        return sort(LST[0:len(LST-1)])
    else:
        return LST
print(sort(lst))
