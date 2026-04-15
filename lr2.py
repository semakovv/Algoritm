# 1
# lst = [0, 1, 2, 3]
# sm = 0
# n = 0
# def func_for(lst1):
#     sm1 = 0
#     for i in lst1:
#         sm1 += i
#     return sm1
# print(func_for(lst))
# def func_while(lst2):
#     sm2 = 0
#     n2 = 0
#     while n2 != len(lst2):
#         sm2 += lst2[n2]
#         n2 += 1
#     return sm2
# print(func_while(lst))
# def func_return(lst3, sm3 = 0, n3 = 0):
#     if n3 != len(lst3):
#         sm3 += lst3[n3]
#         n3 += 1
#         return func_return(lst3, sm3, n3)
#     else:
#         return sm3
# print(func_while(lst))
# 2
# import random
# lst = [random.randint(-9, 9) for i in range(random.randrange(10))]
# print(lst)
# # lst = [3, 2, 1, 0] # сложность алгоритма и быстрая сортировка
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
# import random #число сочитаний из НПК или кол-во рёбер в полном графе
# lst = [random.randint(5, 9) for i in range(random.randrange(10))]
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
# 4
# import random # str to set
# num = random.randint(0, 999)
# print(num)
# def int_num(NUM):
#     # A = {int(i) for i in str(NUM)} # через перебор символов
#     # ln_A = len(A)
#     A = set() # через перебор цифр
#     ln_int_num = len(str(NUM))
#     for i in range(ln_int_num - 1, -1, -1):
#         A.add((NUM // 10 ** i) % 10)
#     ln_A = len(A)
#     return A, ln_A
# print(int_num(num))
# 5
# s = "1 2 3 4 5 5" #
# A = set(s)
# print(A)
# for i in A:
#     cnt = 0
#     for j in s:
#         if (i is j) and (i is not" "):
#             cnt += 1
#     if cnt >= 2:
#         print(i, cnt, "YES")
#     else:
#         print(i, cnt, "NO")
# 6
s = "a a a b b b c c c 1 2 3"
cnt = {i: s.count(i) for i in s}
print(cnt)
