#第一种递归法
# def febo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return(febo(n-2)+febo(n-1))
#
# list =[]
# for i in range(1,21):
#     list.append(febo(i))
# print(list)

#第二种同时赋值
a = 0
b = 1
list = []
n = 1
while n < 21:
    a, b = b, a + b#同时赋值
    list.append(a)
    n+=1
print(list)




