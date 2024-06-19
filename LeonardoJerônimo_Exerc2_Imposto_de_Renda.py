def calcular_salario(salario):
    imposto = 0
    imposto = float()
    if salario >= 2259.21 and salario <= 2826.65:
        imposto = (salario * 0.075) - 169.44
    elif salario >= 2826.66 and salario <= 3751.05:
        imposto = (salario * 0.15) - 381.44
    elif salario >= 3751.06 and salario <= 4664.68:
        imposto = (salario * 0.225) - 662.77
    elif salario > 4664.68:
        imposto = (salario * 0.275) - 896.00
    return imposto

print("Vamos calcular o seu IR!")
salario = float(input("Digite seu salário (separe por .): "))
calcular_salario(salario)

if calcular_salario(salario) == 0:
    print("Você não precisar pagar o IR!")
else:
    print(f"O total a pagar do seu IR é de R$ {calcular_salario(salario):.2f}")
