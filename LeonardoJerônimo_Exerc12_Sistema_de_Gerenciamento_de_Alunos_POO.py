class Aluno:
    def __init__(self, nome: str, matricula: int, curso: str, email: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.email = email
    def __repr__(self):
        return (f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Curso: {self.curso}\n"
                f"Email: {self.email}\n" + "="*10)
    
class SistemaDeCadastro:
    def __init__(self):
        self.alunos = []
    
    def cadastrar_aluno(self):
        while True:
            nome = input("Digite o nome do aluno: ")
            matricula = int(input("Digite a matrícula do aluno: "))
            curso = input("Digite o curso do aluno: ")
            email = input("Digite o email do aluno: ")

            for aluno in self.alunos:
                if aluno.matricula == matricula:
                    print("Matricula já existe!")
                    return
            else:
                novo_aluno = Aluno(nome, matricula, curso, email)
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
        


sistema = SistemaDeCadastro()

while True:
    print("Escolha uma das opções abaixo")
    print("Cadastrar aluno - 1")
    print("Listar aluno - 2")
    print("Buscar aluno - 3")
    print("Excluir aluno - 4")
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
        case _:
            print("Opção inválida")

