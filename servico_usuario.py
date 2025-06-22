class ServicoUsuario:
    def __init__(self, banco):
        self.banco = banco

    def cadastrar_usuario(self, nome, email, senha):
        id = len(self.banco.usuarios) + 1
        usuario = Usuario(id, nome, email, senha)
        self.banco.salvar('usuarios', usuario)
        return usuario

    def autenticar_usuario(self, email, senha):
        for usuario in self.banco.usuarios.values():
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None

    def atualizar_usuario(self, id, nome=None, email=None, senha=None):
        usuario = self.banco.usuarios.get(id)
        if usuario:
            usuario.atualizar(nome, email, senha)
            self.banco.salvar('usuarios', usuario)
            return usuario
        return None

    def excluir_usuario(self, id):
        self.banco.deletar('usuarios', id) 