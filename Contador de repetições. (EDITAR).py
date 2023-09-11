lista=[]
rep=[]
maior=0
for i in range(0,4):
    x=int(input("Digite um número: "))
    lista.append(x)
    if x>maior:
        maior=x
    rep.append(lista.count(x))
print(f"O número {lista[0]} repetiu {rep[0]} vez(es) até agora.")
print(f"O número {lista[1]} repetiu {rep[1]} vez(es) até agora.")
print(f"O número {lista[2]} repetiu {rep[2]} vez(es) até agora.")
print(f"O número {lista[3]} repetiu {rep[3]} vez(es).")

