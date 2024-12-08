from numpy import loadtxt
data=loadtxt('data.txt', dtype=int)
print(data)
Summa=0
s=0
w=[0]*(len(data[1])-1)
print(w)
stop=0
while True:
    s+=1
    i=s%4-1
    Summa=0
    for j in range(len(data[i])-1):
        Summa+=(w[j]*data[i][j])
    if Summa>=0:
        k=1
    else:
        k=0
    if k!=data[i][-1] and Summa>=0:
        for j in range(len(data[i])-1):
            w[j]=w[j]-data[i][j]
        stop=3
    elif k!=data[i][-1] and Summa<0:
        for j in range(len(data[i])-1):
            w[j]=w[j]+data[i][j]
        stop=1
    else:
        stop+=1
    if stop==len(data):
        break
Summa=0
for i in range(len(data[1])-1):
    Summa+=int(input('x:'))*w[i]
if Summa>=0:
    print("Yangi obekt toq sinfga tegishli")
else:
    print("Yangi obekt juft sinfga tegishli")