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
# import random
# lst = [random.randint(-9, 9) for i in range(random.randrange(10))]
# print(lst)
# # lst = [3, 2, 1, 0]
# def sort(LST):
#     swap = False
#     ln_lst = len(LST) - 1
#     for i in range(ln_lst):
#         if LST[i] > LST[i + 1]:
#             LST[i], LST[i + 1] = LST[i + 1], LST[i]
#             swap = True
#     if swap:
#         return sort(LST)
#     else:
#         return LST
# print(sort(lst))
# 3
# import random
# lst = [random.randint(-9, 9) for i in range(random.randrange(10))]
# print(lst)
# # lst = [3, 3, 3, 1, 1, 0]
# def count_twice(LST):
#     # cnt = {i: LST.count(i) for i in LST} кол-во элементов
#     cnt = 0
#     ln_lst = len(LST)
#     for i in range(ln_lst - 1, -1, -1):
#         for j in range(i - 1, -1, -1):
#             if LST[i] == LST[j]:
#                 cnt += 1
#     return cnt
# print(count_twice(lst))
