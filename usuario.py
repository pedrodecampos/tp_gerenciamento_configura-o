class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar(self, banco):
        banco.salvar('usuarios', self)

    def autenticar(self, senha):
        return self.senha == senha

    def atualizar(self, nome=None, email=None, senha=None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
        if senha:
            self.senha = senha

    def excluir(self, banco):
        banco.deletar('usuarios', self.id) 