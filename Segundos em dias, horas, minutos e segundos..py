seg = int(input("Digite a quantidade de segundos: "))
dias = seg // 86400
restoseg = seg % 86400# ele vai dividir e pegar o resto pra si.
horas = restoseg // 3600
restoseg = restoseg % 3600
min = restoseg // 60
restoseg = restoseg % 60
print(f"Dias: {dias}, Horas {horas}, Minutos {min} e Segundos {restoseg}")
