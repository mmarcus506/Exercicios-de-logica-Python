n = int(input("Digite a quantidade de números: "))
lista = []
listamaior = []
listamenor = []
soma = 0
for i in range(n):
    x = float(input("Digite o número: "))
    lista.append(x)
    soma = soma + x
media = soma/n
for k in range(n):
    if lista[k] > media:
        listamaior.append(lista[k])
    elif lista[k] < media:
        listamenor.append(lista[k])
    else:
        continue
maior = min(listamaior)
menor = max(listamenor)
if (maior-media) > (media-menor):
    print(f"O valor mais próximo é {menor}")
elif (media-menor) > (maior-media):
    print(f"O valor mais próximo é {maior}")
else:
    print(f"O valor mais próximo é {media}")