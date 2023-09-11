lista=[]
mini_lista=[]
while True:
    x=(str(input("Digite A para adicionar telefones na agenda, e B para procurar um telefone: ")))
    if x=="A":
        nome=str(input("Digite um nome: "))
        numero=str(input("Digite um número (com 9 na frente e hífen entre): "))
        mini_lista.append(nome)
        mini_lista.append(numero)
        lista.append(mini_lista)
        lista.sort()
        mini_lista=[]
        print(lista)
    if x=="B":
        pesq=str(input("Digite um nome para pesquisa: "))
        for i in range(len(lista)):
            if lista[i][0]==pesq:
                print(f"{lista[i][1]}")
                break
            else:
                print("Estamos Procurando. Por favor, aguarde.")


