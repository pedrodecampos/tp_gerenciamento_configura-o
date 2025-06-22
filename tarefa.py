class Tarefa:
    def __init__(self, id, descricao, usuario_id, categoria_id, concluida=False):
        self.id = id
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id
        self.concluida = concluida

    def criar(self, banco):
        banco.salvar('tarefas', self)

    def atualizar(self, descricao=None):
        if descricao:
            self.descricao = descricao

    def excluir(self, banco):
        banco.deletar('tarefas', self.id)

    def marcar_como_concluida(self):
        self.concluida = True

    @staticmethod
    def listar_por_usuario(banco, usuario_id):
        return [tarefa for tarefa in banco.tarefas.values() if tarefa.usuario_id == usuario_id] 