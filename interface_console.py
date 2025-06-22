class InterfaceConsole:
    def mostrar_menu(self):
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Criar tarefas")
        print("4 - Listar tarefas do usuário logado")
        print("5 - Marcar tarefa como concluída")
        print("0 - Sair")

    def ler_entrada(self, mensagem):
        return input(mensagem)

    def exibir_mensagem(self, mensagem):
        print(mensagem) 