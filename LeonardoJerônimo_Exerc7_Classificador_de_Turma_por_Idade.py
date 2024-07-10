idades = []
while True:
    idade = int(input("Digite uma idade, caso queira parar de adicionar idades digite 0: "))
    if idade == 0:
        break
    idades.append(idade)

soma = sum(idades)
tamanho = len(idades)

resultado = soma // tamanho


print(resultado)

estado = {"Jovem": list(range(25+1)),
          "Adulta": list(range(26,60+1)),
          "Idosa": list(range(60,130))
          }

for chave, valor in estado.items():
    if resultado in valor:
        print(f"A média das idades é: {chave}")