# 1 # не понял
# age = int(input("Введите год: "))
# if age % 4 == 0 and age % 100 != 0 and age % 400 == 0:
#     print("YES")
# else:
#     print("NO")
# 2 #
# n = int(input("Введите кол-во пингвинов: "))
# if 1 <= n <= 9:
#     print("   _~_   " * n)
#     print("  (o o)  " * n)
#     print(" /  V  \ " * n)
#     print(" /( _ )\ " * n)
#     print("  ^^ ^^  " * n)
# 3 #
# s = input("Введите строку: ")
# s = "*".join(s)
# print(s)
# 4 #
# flag = True
# ip = input("Введите IP-адрес: ")
# ip = ip.split(".")
# for i in ip:
#     if i.isdigit() and 0 <= i <= 255:
#         flag = True
#     else:
#         flag = False
#         break
# if flag == True:
#     print("YES")
# else:
#     print("NO")
# 5 #
# import re
# s = input("Введите строку: ")
# a =  re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", s)
# a = "".join(a).lower()
# if a[::] == a[::-1]:
#     print("YES")
# else:
#     print("NO")
