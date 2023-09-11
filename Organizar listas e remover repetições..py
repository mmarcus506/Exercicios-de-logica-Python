vet1=[]
x=1
while x!=0:
    x=int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if x==0:
        break
    else:
        vet1.append(x)
vet2=[]
y=1
while y!=0:
    y=int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if y==0:
        break
    else:
        vet2.append(y)
vet3=[]
for i in range(len(vet1)):
    if vet1[i] not in vet3:
        vet3.append(vet1[i])
    else:
        continue
for j in range(len(vet2)):
    if vet2[j] not in vet3:
        vet3.append(vet2[j])
    else:
        continue
vet3_ord=[]
espelho=[]
for q in range(len(vet3)):
    espelho.append(vet3[q])
for k in range(len(vet3)):
    vet3_ord.append(min(espelho))
    espelho.pop(espelho.index(min(espelho)))
print("Vetor 1:")
print(vet1)
print("Vetor 2:")
print(vet2)
print("Vetor 3:")
print(vet3)
print("Vetor 3 ordenado:")
print(vet3_ord)
