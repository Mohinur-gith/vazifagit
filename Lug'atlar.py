users={1:"ALi",2:"Vali",3:"Qani"}
elements={"Book":"Kitob","All":"Hammasi","End":"Tamom"}
print(elements)
objects={1:"Tom","2":True,3:100.6}
print(objects)
users_list=[["2323324","Ali"],
["343434","Vali"],
["232334","G'ani"]]
users_dict=dict(users_list)
print(users_dict)
users_tuple=(("2323324","Ali"),
("343434","Vali"),
("232334","G'ani"))
users_dict=dict(users_tuple)
print(users_dict)
users={"Bir":"Ali", "Ikki":"Bobur", "Uch":"Alisher" }
print(users["Bir"])
users["Uch"]="Baxtiyor"
print(users["Uch"])

bahoDict={"A":5,"B":4,"C":3}
key="D"
if key in bahoDict:
    baho=bahoDict[key]
    print(baho)
else:
    print("Element topilmadi")

bahoDict={"A":5,"B":4,"C":3}
key="A"
baho=bahoDict.get(key)
print(baho)
key="D"
baho=bahoDict.get(key, "Noma'lum qiymat")
print(baho)

bahoDict={"A":5,"B":4,"C":3,"D":2}
baho="A"
if baho in bahoDict:
    son=bahoDict[baho]
    del bahoDict[baho]
    print(son,"O'chirildi")
else:
    print("Element topilmadi")

bahoDict={"A":5,"B":4,"C":3,"D":2}
key="A"
baho=bahoDict.pop(key)
print(baho)
baho2=bahoDict.pop(key,"Bunday baho mavjud emas")
print(baho2)

l={"ismi":"Sardor","Yoshi":22}
l2={"kursi":1,"yo'nalishi":"TMI"}
l.update(l2)
print(l)
print(l2)

talabalar={"2442423":"Ali", "4546545":"Vali", "2343242":"Alisher"}
for tal in talabalar:
    print(tal," - ",talabalar[tal])
for nomer, ism in talabalar.items():
    print(nomer," - ",ism)
print("Kalitlar:")
for kalit in talabalar.keys():
    print(kalit,end=";")
    print("\n Qiymatlar:")
for qiymat in talabalar.values():
    print(qiymat,end=";")

loginData={ "Ali": { "email":"ali@gmail.com", "tel":"2323235", "manzil":"Toshkent" },
            "Vali": { "email":"ali@gmail.com", "tel":"2323835", "manzil":"Jizzax" }}
print(loginData)