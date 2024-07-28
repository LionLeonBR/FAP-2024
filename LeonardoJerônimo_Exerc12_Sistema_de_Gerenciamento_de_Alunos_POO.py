class Aluno:
    def __init__(self, nome: str, matricula: int, curso: str, media: float, notas= None) -> None:
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas if notas is not None else []
        self.media = media

    def __repr__(self):
        return (f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Curso: {self.curso}\n"
                f"Notas: {self.notas}\n"
                f"Media: {self.media:.2f}\n" + "="*10)
    
class SistemaDeCadastro:
    def __init__(self):
        self.alunos = []
    
    def cadastrar_aluno(self):
        while True:
            nome = input("Digite o nome do aluno: ")
            matricula = int(input("Digite a matrícula do aluno: "))
            curso = input("Digite o curso do aluno: ")
            notas = []

            while True:
                nota = int(input("Digite uma nota ou -1 para sair: "))
                if nota == -1:
                    break
                elif nota < 0 or nota > 10:
                    print("As notas devem estar entre 0 e 10! ")
                    continue 
                notas.append(nota)

            media = sum(notas) / len(notas) 

            for aluno in self.alunos:
                if aluno.matricula == matricula:
                    print("Matricula já existe!")
                    return
            else:
                novo_aluno = Aluno(nome, matricula, curso, media, notas)
                self.alunos.append(novo_aluno)
                print("Aluno cadastrado!")

            continuar = input("Deseja cadastrar outro aluno? (s/n): ")
            if continuar.lower() != 's':
                break  

    def listar_alunos(self):

        if not self.alunos:
            print("Nenhum aluno cadastrado")
        else:
            for aluno in self.alunos:
                print(aluno)

    def buscar(self, matricula: int):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None
    
    def excluir(self, matricula: int):
        aluno = self.buscar(matricula)
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                print(f"Aluno com a matricula {matricula} foi excluido!")
                return
        print(f"Aluno com a matricula {matricula} não encontrado.")

    def editar(self, matricula: int):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                while True:
                    print("===Opção que deseja alterar===")
                    print("==[1] Nome")
                    print("==[2] Matricula")
                    print("==[3] Curso")
                    print("==[4] Notas")
                    print("==[0] Sair")
                    opcao_a = int(input("Selecione: "))
                    match opcao_a:
                        case 0:
                            break
                        case 1:
                            aluno.nome = input("Novo nome: ")
                            print("Nome alterado com sucesso!")
                        case 2:
                            n_matricula = int(input("Nova matricula: "))
                            if any(a.matricula == n_matricula for a in self.alunos):
                                print("A matrícula já existe!")
                            else:
                                aluno.matricula = n_matricula
                                print("Matricula alterada com sucesso!")
                            
                        case 3:
                            aluno.curso = input("Novo curso: ")
                            print("Curso alterado com sucesso!")
                        case 4:
                            while True:
                                notas = []
                                nota = int(input("Digite uma nota ou -1 para sair: "))
                                if nota == -1:
                                    break
                                elif nota < 0 or nota > 10:
                                    print("As notas devem estar entre 0 e 10! ")
                                    continue 
                                notas.append(nota)
                            aluno.notas = notas
                            aluno.media = sum(notas) / len(notas)
                            print("Notas alteradas com sucesso!")
        else:
            print("Aluno não encontrado!")

        


sistema = SistemaDeCadastro()

while True:
    print("Escolha uma das opções abaixo")
    print("Cadastrar aluno - 1")
    print("Listar aluno - 2")
    print("Buscar aluno - 3")
    print("Excluir aluno - 4")
    print("Editar aluno - 5")
    print("Sair - 0")
    opcao = int(input())
    
    match opcao:
        case 0:
            break
        case 1:
            sistema.cadastrar_aluno()
        case 2:
            sistema.listar_alunos()
        case 3:
            matricula = int(input("Matricula do aluno: "))
            aluno = sistema.buscar(matricula)
            if aluno:
                print("Aluno encontrado!")
                print(aluno)
            else:
                print("Aluno não encontrado")
        case 4:
            matricula = int(input("Matricula do aluno que deseja excluir: "))
            sistema.excluir(matricula)
        case 5:
            matricula = int(input("Matricula do aluno que deseja editar: "))
            sistema.editar(matricula)

        case _:
            print("Opção inválida")
