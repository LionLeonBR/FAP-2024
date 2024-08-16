alunos = []
resete = 0
while True:
    print("### Menu de Cadastro de Alunos")
    print("[1] Cadastrar novo aluno")
    print("[2] Listar alunos cadastrados")
    print("[3] Editar aluno")
    print("[4] Excluir aluno")
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
            # retorna ao zero para não pular para sempre depois da primeira mudança
            resete = 0
            continue
        novo_aluno["notas"] = []
        while True:
            nota = int(input("Digite uma nota ou digite '-1' parar: "))
            if nota == -1:
                break
            novo_aluno["notas"].append(nota)

        novo_aluno["media"] = sum(novo_aluno["notas"]) / len(novo_aluno["notas"])

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
                print(f"Notas:",aluno["notas"])
                print(f"Média:",aluno["media"])
                print("-----------------------------------")
    elif opcao == 3:
        matricula = int(input("Digite a matricula do aluno: "))
        for aluno in alunos:
            if matricula == aluno['matricula']:
                while True:
                    print('[1] Alterar Nome')
                    print('[2] Alterar Curso')
                    print('[3] Alterar Matrícula')
                    print('[4] Alterar Notas')
                    print('[0] Sair')
                    editar_opcao = int(input())
                    match editar_opcao:
                        case 0:
                            break
                        case 1:
                            aluno['nome'] = input("Novo nome: ")
                        case 2:
                            aluno['curso'] = input("Novo curso: ")
                        case 3:
                            nova_matricula = int(input("Nova matricula: "))
                            for aluno in alunos:
                                if nova_matricula == aluno['matricula']:
                                    print("A matricula inserida já existe!")
                            else:
                                aluno['matricula'] = nova_matricula
                        case 4:
                            aluno['notas'] = input("Novas notas: ").split()
                            aluno['media'] = sum(aluno["notas"]) / len(aluno["notas"])
        else:
            print("Não encontramos nenhum aluno com essa matricula!")

    elif opcao == 4:
        matricula = int(input("Digite a matricula do aluno que deseja EXCLUIR: "))
        for aluno in alunos:
            if matricula == aluno["matricula"]:
                alunos.remove(aluno)
                print("Aluno removido com sucesso")
                break

        else:
            print("Aluno não encontrado! ")




    elif opcao == 0:
        print("Saindo do programa...")
        break
    if opcao < 0 or opcao > 4:
        print(f"Só existem 0, 1 e 2 como opção, não existe uma opção {opcao}")
