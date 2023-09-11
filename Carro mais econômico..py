#printa o modelo mais econômico digitafo e mostra o quanto ele gasta, considerando a gasolina a 3,50 reais (bem dificil k)
lista=[]
econom=0
n=int(input("Digite a quantidade de carros que você deseja: "))
for i in range(n):
    carros=[]
    modelo = str(input("Modelo: "))
    kmperlitro= float(input("Km/L: "))
    carros.append(modelo)
    carros.append(kmperlitro)
    lista.append(carros)
menor=lista[0][1]
for k in range(n):
    print(f"O modelo {lista[k][0]} gasta R$ {(1000/lista[k][1])*(3.5):,.2f} a cada 1000 km rodados.")
    if lista[k][1]<=menor:
        econom=lista[k][0]
print(f"O modelo mais barato é o(a) {econom}.")
