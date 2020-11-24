p1, p2 = [1, 3, -2], [2, -1, 3]

vetoresRo = []
vetoresR1 = []
t=1
for p in range(len(p1)):
    value1 = 1*p1[p]
    if((p1[p] > 0)):
        value2 = "-t*"+str(p1[p])
    else:
        value2 = "+t*"+str(p1[p]*(-1))
    if(value1 > 0):
        esq = value2+" + "+str(value1)
    else:
        esq = value2+" "+str(value1)
    if(p2[p] < 0):
        value11 = "-t"
    else:
        value11 = "+t*"+str(p2[p])
    vetoresRo.append(esq)
    vetoresR1.append(value11)

print(vetoresRo)
print(vetoresR1)

for i in range(len(vetoresRo)):
    x = (eval(vetoresRo[i].split()[0] + vetoresR1[i]))
    y = (vetoresRo[i].split()[-1])
    w = str(y)+" "+str(x)+("*t")
    print(w)

