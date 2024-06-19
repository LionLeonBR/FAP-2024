# Função entrada
def entrada_de_dados():

    # Banco de dados/Dicionario das bolas
    Bolas_Tamanho_cm = {
                    "Bola de Basquete adulto":24,
                    "Bola de Basquete infantil":22,
                    "Bola de Futebol Oficial":22,
                    "Bola de Vôlei":21,
                    "Bola de Handball":19,
                    "Bola de Futebol de Salão":20,
                    }

    # Entrada para tamanho de bolas
    while True: 
        print("Digite uma das opções abaixo")

        # Lista as bolas
        for bolas in Bolas_Tamanho_cm:
            print(f"-- {bolas}")

        # Entrada do Usuário
        bola = input("Caso deseje uma personalizada digite 'Personalizada': ")

        # Entrada Personalizada do usuário
        if bola == "Personalizada":
            print("Digite o tamanho em centimetros")
            comprimento = int(input("Comprimento: "))
            largura = int(input("Largura: "))
            altura = int(input("Altura ")) 

            # Entrada para tamanho do depósito
            print("Insira as medidas do Depósito em metros: ")
            d_comprimento = float(input("Comprimento: "))
            d_largura = float(input("Largura: "))
            d_altura = float(input("Altura: ")) 
            # Entrega None para manter os 7 argumentos
            return comprimento,largura,altura,d_comprimento,d_largura,d_altura, None
        
        # Entrada não personalizada
        elif bola != "Personalizada" and bola in Bolas_Tamanho_cm:

            # Presente no Banco de dados
            if bola in Bolas_Tamanho_cm:
                print(f"Sua opção escolhida foi: {bola}") 
                volume_bola = Bolas_Tamanho_cm[bola] ** 3
            print("Insira as medidas do Depósito em metros: ")

            # Entrada para tamanho do depósito
            d_comprimento = float(input("Comprimento: "))
            d_largura = float(input("Largura: "))
            d_altura = float(input("Altura: "))
            # Entrega None para manter os 7 argumentos
            return None, None, None, d_comprimento, d_largura, d_altura, volume_bola
        
        # Não presente no Bando de dados
        else:
            print(f"{bola}, Não existe em nosso banco de dados")
            print("Porfavor certifique-se que digitou corretamente")
            print("caso contrário selecione a opção 'Personalizada'")
# Função Calculo
def calcular_volume(altura,largura,comprimento,d_comprimento,d_largura,d_altura,volume_bola):
    # Volume
    volume_deposito = (d_comprimento * d_largura * d_altura) * 100
    # Escolha da bola, se é personalizada ou não
    if volume_bola is not None:
        # No caso a bola está no banco de dados
        return volume_bola, volume_deposito
    else: 
        # A bola não está no banco de dados, calculando o volume da nova
        volume_bola_personalizado = comprimento * largura * altura
        return volume_bola_personalizado, volume_deposito
# Função calcular o total e entregar resposta
def total_cabido(volume_bola,volume_deposito):
    # o quanto "cabido" é o quanto coube dentro do deposito
    cabido = volume_deposito // volume_bola
    # caso a bola seja maior que o depósito
    if volume_deposito < volume_bola:
        print("O espaço do deposito é inferior ao espaço da bola, verifique se os dados foram colocados corretamente")
        # Return para fazer a recursão
        return 1
    else:
        print(f"O numero total de bolas que caberão no deposito será de aproximadamente: {cabido} bolas")
        # Return para parar a recursão
        return 0   
# Repete até os dados estarem ok
def repete():
    while True:
        # Dados salvos em uma lista
        dados = entrada_de_dados()
        # Variaveis que seram salvas dos dados desempacotados do Calcular volume, *dados é para desempacotar conteudos de uma lista
        volume_bola, volume_deposito = calcular_volume(*dados)
        # O valor que sair dentro da função ditará se repetirá ou não
        repetir = total_cabido(volume_bola, volume_deposito)
        # Parar a recursão
        if repetir == 0:
            break
# Inicio o processo
repete()