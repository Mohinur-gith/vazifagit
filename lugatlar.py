import numpy as np
a = np.array([[1, 0, 0],[1, 1, 1],[2, 0, 0]])
b = np.array([[1, 1, 1],[1, 1, 2],[1, 1, 2]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

a = np.array([1, 2, 3], dtype=np.int16)
print(a) # [1 2 3]
print(a.dtype) # int16
b = np.array([1, 2, 3], dtype=np.float64)
print(b) # [1. 2. 3.]
print(b.dtype) # float64

a = np.zeros((2,3), dtype=np.int16)
print(a)
print(a.dtype)

a = np.linspace(0.5, 9.5, 10)
print(a)
# [0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5]
b = np.linspace(0.5, 9.5, 5)
print(b)
# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()
#
# n=int(input("n= "))
# m=int(input("m= "))
# a=[]
# for x in range(n):
#     c=[]
#     for y in range(m):
#         c.append(int (input("Elementlarni kiriting: ")))
#     a.append(c)
# print(a)
#
# array_2d = [[int(input("Elementni kiriting:")) for x in range(2)] for y in range(3)]
# print(array_2d)

# import numpy as np
# a = np.array([1, 2, 3])
# print("Birinchi massiv",a)
# b = np.array([[1, 2], [3, 4]])
# print("Ikkinchi massiv",b)
# c = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
# print("Uchinchi massiv",c)
# for r in c:
#     for i in r:
#         for k in i:
#             print(k, end=" ")
#     print()