n=int(input("Quantos mercados temos próximo de maria? "))
menor=1001
mercado=0
merc_barato=0
for i in range(0, n):
    p = float(input("Preço da carne em P BITS: "))
    g = int(input("Quantidade de gramas: "))
    preco_per_g = p / g
    mercado += 1
    if preco_per_g < menor:
        menor = preco_per_g
        merc_barato = mercado
print(f"O preço para comprar 1 kg de carne é {menor*1000:,.2f} no mercado de número {merc_barato}")

