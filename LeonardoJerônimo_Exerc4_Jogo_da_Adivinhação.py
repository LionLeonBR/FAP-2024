from random import randint

print("Jogo da advinhação vamos lá!")
pc = randint(1,50)
tentativas = 1


while True:
    usuario = input("Digite seu numero: ")
    try:
        usuario = int(usuario)
    except:
        print("Você não digitou um numero, digite um numero entre 1 e 50")
        continue

    if usuario < 1 or usuario > 50:
        print("O numero que você digitou é invalido selecione entre 1 e 50")
        continue
    else:
        if usuario == pc:
            print(f"Parabens você conseguiu após {tentativas}")
            break
        elif usuario < pc:
            print("ERROOO! Tente novamente: ")
            print("Dica: É maior que isso")
        elif usuario > pc:
            print("ERROOO! Tente novamente")
            print("Dica: é menor que isso")
            tentativas += 1
  

