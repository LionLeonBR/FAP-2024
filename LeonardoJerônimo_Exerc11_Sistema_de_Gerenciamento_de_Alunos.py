alunos = []
resete = 0
while True:
    print("### Menu de Cadastro de Alunos")
    print("[1] Cadastrar novo aluno")
    print("[2] Listar alunos cadastrados")
    print("[0] Sair")

    opcao = input("Selecione sua opção: ")

    try:
        opcao = int(opcao)
    except:
        print("O valor que você digitou não é um número!")
        continue

    if opcao == 1:
        novo_aluno = {}

        novo_aluno["nome"] = input("Nome do aluno: ")
        novo_aluno["curso"] = input("Curso: ")
        # validação de dados
        if novo_aluno["nome"] == "" or novo_aluno["curso"] == "":
            print("O nome e o curso não podem estar vazios!")
            continue
        novo_aluno["matricula"] = input("Matricula: ")
        try:
            novo_aluno["matricula"] = int(novo_aluno["matricula"])
        except:
            print("A matricula informada deve ser um número!")
            continue
        for aluno in alunos:
            if novo_aluno["matricula"] == aluno["matricula"]:
                print("A matricula já está cadastrada no sistema!")
                resete = 1
                break
        # reset caso encontre a mesma matricula
        if resete == 1:
            continue
        novo_aluno["notas"] = input("Notas:").split(" ")

        alunos.append(novo_aluno)
        print("Cadastrado com sucesso!")
    elif opcao == 2:
        if len(alunos) == 0:
            print("Ainda não há alunos cadastrados")
        else:
            for aluno in alunos:
                print("Nome:", aluno["nome"])
                print(f"Curso:",aluno["curso"])
                print(f"Matrícula:",aluno["matricula"])
                print("-----------------------------------")
    elif opcao == 0:
        print("Saindo do programa...")
        break
    if opcao < 0 or opcao > 2:
        print(f"Só existem 0, 1 e 2 como opção, não existe uma opção {opcao}")