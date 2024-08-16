dnv = "sim"
while dnv == "sim":
    print("Celsius para Fahrenheit ou Fahrenheit para Celsius")
    tipo = input("Digite 1 ou 2: ")
    try:
        tipo = int(tipo)
    except:
        print("Você não digitou um numero, Digite 1 ou 2")
        continue
    if tipo > 2 or tipo < 1:
        print("Só existem 2 opções: 1 e 2, por favor, selecione uma das duas")
        continue
    if tipo == 1:
        temperatura = "Celsius"
        temp = input(f"Valor em {temperatura}: ")
        try:
            temp = int(temp)
        except:
            print("Valor digitado não é um numero inteiro, digite um numero inteiro")
            continue

        valor = (temp * (9/5)) + 32
        print(f"O valor em {temperatura} para Fahrenheit é: {valor}°F")
        dnv = input("Deseja fazer fazer outra conversão? sim ou não: ")


    elif tipo == 2:
        temperatura = "Fahrenheit"       
        temp = input(f"Valor em {temperatura}: ")
        try:
            temp = int(temp)
        except:
            print("Valor digitado não é um numero inteiro, digite um numero inteiro")
            continue
        valor = (temp - 32) * (5/9)
        print(f"O valor em {temperatura} para Fahrenheit é: {valor:.1f}°C")
        dnv = input("Deseja fazer fazer outra conversão? sim ou não: ")
print("Obrigado! ^^")
