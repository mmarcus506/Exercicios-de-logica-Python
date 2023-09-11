maior=menor=cont=0
x="s"
while x in "s":
    n=int(input("Digite um número qualquer: "))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if  n > maior:
            maior = n
        if n < menor:
            menor = n
    x = str(input("Deseja continuar? (s/n) "))

print(f"O maior valor é {maior} e o menor é {menor}")