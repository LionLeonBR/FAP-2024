#  "Telefonou para a vítima?"
#  "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  "Devia para a vítima?"
#  "Já trabalhou com a vítima?"
# O programa deve classificar a pessoa como:
#  "Inocente": 0-1 respostas positivas
#  "Suspeita": 2 respostas positivas
#  "Cúmplice": 3-4 respostas positivas
#  "Assassino": 5 respostas positivas

perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?",            
             ]

situação = {"Inocente": [0,1],
            "Suspeita": [2],
            "Cúmplice": [3,4],
            "Assasino": [5]
            }

respostas = 0

for pergunta in perguntas:
    resposta = input(f"{pergunta} s/n")
    if resposta == "s":
        respostas = respostas + 1

for chave, valores in situação.items():
    if respostas in valores:
        print(f"Você é {chave} ")
