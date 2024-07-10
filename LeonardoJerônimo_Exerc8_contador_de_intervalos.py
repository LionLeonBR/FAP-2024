intervalos = {"Primeiro Intervalo": list(range(0,25+1)),
              "Segundo Intervalo": list(range(26,50+1)),
              "Terceiro Intervalo": list(range(51,75+1)),
              "Quarto Intervalo": list(range(76,100+1))
              }
qntd_intervalos = {"Primeiro Intervalo": [],
                   "Segundo Intervalo": [],
                   "Terceiro Intervalo": [],
                   "Quarto Intervalo": []
                   }

while True:
    numero = int(input("Digite um numero entre 1 a 100, digite um negativo para sair: "))
    if numero < 0:
        break
    if numero > 100:
        print("Entre 1 e 100")
        continue
    for chave, valor in intervalos.items():
        if numero in valor:
            print(f"seu numero está presente no {chave}")
            qntd_intervalos[f"{chave}"].append(numero)

for chave, valor in qntd_intervalos.items():
    print(f"Existem {len(valor)} no {chave}")
    
