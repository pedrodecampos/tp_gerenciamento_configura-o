from usuario import Usuario
from tarefa import Tarefa
from banco_de_dados import BancoDeDados

class App:
    def __init__(self):
        self.banco = BancoDeDados()
        self.usuario_atual = None

    def iniciar(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Cadastrar usuário")
            print("2 - Login")
            print("3 - Criar tarefa")
            print("4 - Listar tarefas do usuário logado")
            print("5 - Marcar tarefa como concluída")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.login()
            elif opcao == "3":
                self.criar_tarefa()
            elif opcao == "4":
                self.listar_tarefas_usuario()
            elif opcao == "5":
                self.marcar_tarefa_concluida()
            elif opcao == "0":
                self.encerrar()
                break
            else:
                print("Opção inválida!")

    def encerrar(self):
        print("Encerrando o sistema. Até logo!")

    def cadastrar_usuario(self):
        print("\n--- Cadastro de Usuário ---")
        id = len(self.banco.usuarios) + 1
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        usuario = Usuario(id, nome, email, senha)
        self.banco.salvar('usuarios', usuario)
        print("Usuário cadastrado com sucesso!")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ")
        senha = input("Senha: ")
        for usuario in self.banco.usuarios.values():
            if usuario.email == email and usuario.senha == senha:
                self.usuario_atual = usuario
                print(f"Bem-vindo, {usuario.nome}!")
                return
        print("Usuário ou senha incorretos!")

    def criar_tarefa(self):
        if not self.usuario_atual:
            print("Você precisa estar logado para criar tarefas.")
            return
        print("\n--- Criar Tarefa ---")
        id = len(self.banco.tarefas) + 1
        descricao = input("Descrição da tarefa: ")
        tarefa = Tarefa(id, descricao, self.usuario_atual.id, 1)
        self.banco.salvar('tarefas', tarefa)
        print("Tarefa criada com sucesso!")

    def listar_tarefas_usuario(self):
        if not self.usuario_atual:
            print("Você precisa estar logado para ver suas tarefas.")
            return
        print(f"\n--- Tarefas de {self.usuario_atual.nome} ---")
        encontrou = False
        for tarefa in self.banco.tarefas.values():
            if tarefa.usuario_id == self.usuario_atual.id:
                status = "Concluída" if tarefa.concluida else "Pendente"
                print(f"ID: {tarefa.id} | {tarefa.descricao} | {status}")
                encontrou = True
        if not encontrou:
            print("Nenhuma tarefa encontrada.")

    def marcar_tarefa_concluida(self):
        if not self.usuario_atual:
            print("Você precisa estar logado para marcar tarefas.")
            return
        id_tarefa = input("Digite o ID da tarefa a ser marcada como concluída: ")
        tarefa = self.banco.tarefas.get(int(id_tarefa))
        if tarefa and tarefa.usuario_id == self.usuario_atual.id:
            tarefa.marcar_como_concluida()
            print("Tarefa marcada como concluída!")
        else:
            print("Tarefa não encontrada ou não pertence a você.")

if __name__ == "__main__":
    app = App()
    app.iniciar() 