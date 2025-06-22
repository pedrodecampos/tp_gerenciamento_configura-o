class Tarefa:
    def __init__(self, id, descricao, usuario_id, categoria_id, concluida=False):
        self.id = id
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id
        self.concluida = concluida

    def criar(self):
        pass

    def atualizar(self, descricao=None):
        pass

    def excluir(self):
        pass

    def marcar_como_concluida(self):
        pass

    def listar_por_usuario(self, usuario_id):
        pass 