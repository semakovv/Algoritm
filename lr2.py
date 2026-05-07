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
# 2 оценка сложности алгоритма и быстрая сотрировка O(logn)
# import random as ra
# lst = [ra.randint(-9, 9) for i in range(20)]
# print(lst)
# l = 0
# r = len(lst)
# def sort(LST):
#     i = 0
#     j = len(LST) - 1
#     q = 0
#     while i <= j:
#         while i < len(LST) and LST[i] < q:
#             i += 1
#         while j > 0 and LST[j] > q:
#             j -= 1
#         if i <= j:
#             LST[i], LST[j] = LST[j], LST[i]
#             i += 1
#             j -= 1
# sort(lst)
# print(lst)
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
# 4 str to set
import random
num = random.randint(0, 99999)
print(num)
def int_num(NUM):
    NUM = str(NUM)
    A = set(NUM)
    for i in A:
        print(i, NUM.count(i))
int_num(num)
# 5 
# s = "1 2 3 22 22 4 5 5"
# s = s.split()
# print(s)
# A = set()
# for i in s:
#     if i in A:
#         print(i, "YES")
#     else:
#         A.add(i)
#         print(i, "NO")
# 6
# s = "a a a b b b c c c 1 2 3"
# cnt = {i: s.count(i) for i in s}
# print(cnt)
