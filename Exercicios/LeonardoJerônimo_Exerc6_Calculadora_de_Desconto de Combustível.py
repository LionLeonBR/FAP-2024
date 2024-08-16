#  Álcool: até 20 litros (3% por litro), 
# acima de 20 litros (5% por litro)

#  Gasolina: até 20 litros (4% por litro), 
# acima de 20 litros (6% por litro) Preços

# base: Álcool R$ 1,90/litro, Gasolina R$ 2,50/litro

desconto_A = 0.03
desconto_G = 0.04

desconto_AA = 0.05
desconto_GG = 0.06

p_alcool = 1.90
p_gasolina = 2.50

tipo = int(input("1 para Gasolina 2 para Álcool: "))
quantidade = int(input("Quantidade abastecida: "))

valorDescontado = 0
valor_total = 0

if quantidade <= 20 and tipo == 1:
    valorDescontado = (p_gasolina * quantidade) * desconto_G
    valor_total = (p_gasolina * quantidade) - valorDescontado

    print(f"A quantidade total a pagar é R$ {valor_total} o desconto foi de R$ {valorDescontado:.2f}")
    
elif quantidade <= 20 and tipo == 2:
    valorDescontado = (p_alcool * quantidade) * desconto_A
    valor_total = (p_alcool * quantidade) - valorDescontado

    print(f"A quantidade total a pagar é R$ {valor_total} o desconto foi de R$ {valorDescontado:.2f}")
    
elif quantidade > 20 and tipo == 2:
    valorDescontado = (p_alcool * quantidade) * desconto_AA
    valor_total = (p_alcool * quantidade) - valorDescontado

    print(f"A quantidade total a pagar é R$ {valor_total} o desconto foi de R$ {valorDescontado:.2f}")
    
elif quantidade > 20 and tipo == 1:
    valorDescontado = (p_gasolina * quantidade) * desconto_GG
    valor_total = (p_gasolina * quantidade) - valorDescontado

    print(f"A quantidade total a pagar é R$ {valor_total} o desconto foi de R$ {valorDescontado:.2f}")
    