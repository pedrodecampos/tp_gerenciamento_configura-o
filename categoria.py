class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def criar(self, banco):
        banco.salvar('categorias', self)

    def atualizar(self, nome):
        if nome:
            self.nome = nome

    def excluir(self, banco):
        banco.deletar('categorias', self.id)

    @staticmethod
    def listar_tarefas(banco, categoria_id):
        return [tarefa for tarefa in banco.tarefas.values() if tarefa.categoria_id == categoria_id] 