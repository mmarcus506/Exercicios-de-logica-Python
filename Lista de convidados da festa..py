nome=str(input("Nome do convidado: "))
lista=[]
lista.append(nome)
while nome !="":
    nome = str(input("Deseja adicionar mais um convidado? Se sim, digite o nome. Se não, digite N: "))
    if nome =="N":
        break
    elif nome not in lista:
        lista.append(nome)
    else:
        continue
print(lista)
nome_in_lista =str(input("Deseja pesquisar o nome de algum convidado? S/N "))
while nome_in_lista != "N":
    nome_festa=str(input("Digite o nome do convidado: "))
    if nome_festa in lista:
        print("Pode passar!")
    nome_de_novo = str(input("Deseja pesquisar o nome de mais algum convidado? S/N "))
    if nome_de_novo != "S":
        break


