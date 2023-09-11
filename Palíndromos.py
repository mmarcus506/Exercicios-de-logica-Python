palavra = str(input("Digite uma palavra: ")).upper().strip()
inver = f"{palavra}"[::-1]
print(palavra)
print(inver)
if palavra == inver:
    print("É palíndromo")
else:
    print("Não é palíndromo")
