# try:
#     import math
#     print(math.exp(710))
# except OverflowError:
#     print ("Son xotiradan chiqib ketdi.")
# else:
#     print ("Xatolik yo’q!")

try:
    a = 5 
    b = "Satr"
    c = a + b
except TypeError:
    print ('TypeError xatoligi')
else:
    print ('Xatolik yo’q!')

# try:
#     son1=int(input("son1 = "))
#     son2=int(input("son2 = "))
#     print((son1/son2))
# except ValueError:
#     print("O'girishdagi xatolik")
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas")
# except Exception as e:
#     print("Umumiy xatolik",e)

# try:
#     son1=int(input("Birinchi sonni kiriting:"))
#     son2=int(input("Ikkinchi sonni kiriting:"))
#     if son2==0:
#         raise Exception("Nolga bo'lish yuzaga keldi")
#     print("Bo'lish natijasi:",son1/son2)
# except ValueError:
#     print("O'girish muffaqiyatsiz amalga oshirildi")
# except Exception as e:
#     print("Xatolik",e)
# print("Dastur tugadi")

# from math import sqrt
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
# except ValueError as exp:
#     print("Berilgalarni kiritishda xato:\t", exp)
# D = b * b - 4 * a * c
# if D < 0:
#     print("Tenglamaga haqiyqiy yechimga ega emas!")
# elif D == 0:
#     print("Tenglama bitta yechimga ega:")
#     x = b / (2 * a); print("x = ", x)
# else:
#     print("tenglama ikkita yechimga ega:")
#     x1 = (b + sqrt(D)) / (2 * a)
#     x2 = (b - sqrt(D)) / (2 * a)
#     print("x1 = ", x1, "\nx2 = ", x2)
