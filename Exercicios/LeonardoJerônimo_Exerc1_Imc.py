print("Vamos verificar o seu IMC!")


while True:
    altura = float(input("Insira sua altura (metros): "))
    if altura < 0.6 or altura > 2.5:
        print("Valor inválido! Digite um valor entre 0.6 metros e 2.5 metros!")
    else:
        break

while True:
    peso = float(input("Insira seu peso (kg): "))
    if peso < 15 or peso > 250:
        print("Valor inválido! Digite um peso entre 15kg e 250kg!")
    else:
        break

imc = peso / (altura ** 2)

#Classificação do IMC:
#o Abaixo de 18.5: Abaixo do peso
#o Entre 18.5 e 24.9: Peso normal
#o Entre 25 e 29.9: Sobrepeso
#o Entre 30 e 34.9: Obesidade grau I
#o Entre 35 e 39.9: Obesidade grau II
#o Acima de 40: Obesidade grau III

if imc < 18.5:
    print("Seu indice é: Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu indice é: Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Seu indice é: Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Seu indice é: Obesdidade grau I")
elif imc >= 35 and imc <= 39.9:
    print("Seu indice é: Obesdidade grau II")
else:
    print("Seu indice é: Obesidade grau III")