# user_list=["Ali","Vali",1,-12.34]
# user_tuple=tuple(user_list)
# print(user_tuple)

# user=("Ali","Vali",1,-12.34)
# print(user[0])
# print(user[-1])
# print(user[1:3])

# user=("Ali","Vali","Akmal")
# a,b,c=user
# print(a)
# print(b)
# print(c)

# def get_user():
#     name="Akmal"
#     age=23
#     is_married=True
#     return name, age, is_married
# user=get_user()
# print(user[0])
# print(user[1])
# print(user[2])
# name,age,ismarried=get_user()
# print(name)
# print(age)
# print(ismarried)

# user=("Malik",30,True)
# i=0
# print("for sikli yordamida")
# for u in user:
#     print(u)
# print("while sikli yordamida")
# while i<len(user):
#     print(user[i])
#     i+=1

# davlatlar=(("O'zbekiston",33.8,(("Toshkent",2.65),("Samarqand",1.1),("Urganch",0.223))),
# ("Qozog'iston",17.5,(("Nur Sultan",1.1),("Olmaota",2.3))))
# for davlat in davlatlar:
#     nomi,aholi_soni,shaharlar=davlat
#     print(nomi,'-',aholi_soni)
#     print("Katt shaharlari:")
#     for shahar in shaharlar:
#         print(shahar[0],'-',shahar[1])

def AddStudent():
    global students
    fam = input("Familiya: ")
    ism = input("Ism: ")
    sharif = input("Otasining ismi: ")
    jins = input("Jinsi: ")
    yosh = int(input("Yoshi: "))
    kurs = int(input("Kursi: "))
    new_student = (fam, ism, sharif, jins, yosh, kurs)
    students.append(new_student)
def EditStudent():
    global students
    fam = input("Tahrirlamoqchi bo'lgan familyangizni tanlang: ")
    for item in students:
        if fam.lower() == item[0].lower():
            print("Enter the data of editing student")
            item[0] = input("Familiya: ")
            item[1] = input("Ism: ")
            item[2] = input("Otasining ismi: ")
            item[3] = input("Jinsi: ")
            item[4] = int(input("Yoshi: "))
            item[5] = int(input("Kursi: "))
            break
def DeleStudent():
    global students
    fam = input("O'chirmoqchi bo'lgan familyangizni tanlang: ")
    for item in students:
        if fam.lower() == item[0].lower():
            students.remove(item)
            break
def PrintAll():
    global students
    for item in students:
        print(item)
def PrintLastStudent():
    pass
def PrintMostMen():
    pass
def PrintTheMostNames():
    pass
def PrintEquallyNamesWomen():
    pass
def PrintSeprateByCourseNumbers():
    pass
def Print(students):
    print("Familiyasi: ", students[0])
    print("Ismi: ", students[1])
    print("Sharifi: ", students[2])
    print("Jinsi: ", students[3])
    print("Yoshi: ", students[4])
    print("Kursi: ", students[5])
while True:
    print("Buyruqlar:")
    print("1-Yangi talaba qo'shish")
    print("2-Tahririlash")
    print("3-O'chirish")
    print("4-Oxirgi talabani chiqarish")
    print("5-Erkaklar soni eng ko'p bo'lgan kurs nomeri")
    print("6-Eng ko‘p tarqalgan erkak va ayollar ismlari")
    print("7-Yoshi va ismi bir xil bo‘lgan talaba qizlar familiyalarining  alfavit tartibidagi royxati")
    print("8-Ro‘yxat kurslarga ajratilsin")
    print("9-Talabalar ro'yxatini chop etish")
    print("0-Chiqish")
    command = int(input("Buyruq raqamini kiriting: "))
    if command == 1:
        AddStudent()
        continue
    if command == 2:
        EditStudent()
        continue
    if command == 3:
        DeleStudent()
        continue
    if command == 4:
        PrintLastStudent()
        continue
    if command == 5:
        PrintMostMen()
        continue
    if command == 6:
        PrintTheMostNames()
        continue
    if command == 7:
        PrintEquallyNamesWomen()
        continue
    if command == 8:
        PrintSeprateByCourseNumbers()
        continue
    if command == 9:
        Print()
        continue
    if command == 0:
        break