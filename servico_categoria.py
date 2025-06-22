class ServicoCategoria:
    def __init__(self, banco):
        self.banco = banco

    def criar_categoria(self, nome):
        id = len(self.banco.categorias) + 1
        categoria = Categoria(id, nome)
        self.banco.salvar('categorias', categoria)
        return categoria

    def atualizar_categoria(self, id, nome):
        categoria = self.banco.categorias.get(id)
        if categoria:
            categoria.atualizar(nome)
            self.banco.salvar('categorias', categoria)
            return categoria
        return None

    def excluir_categoria(self, id):
        self.banco.deletar('categorias', id)

    def listar_tarefas_da_categoria(self, categoria_id):
        return [tarefa for tarefa in self.banco.tarefas.values() if tarefa.categoria_id == categoria_id] 