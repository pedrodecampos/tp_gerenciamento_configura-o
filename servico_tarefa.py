class ServicoTarefa:
    def __init__(self, banco):
        self.banco = banco

    def criar_tarefa(self, descricao, usuario_id, categoria_id):
        id = len(self.banco.tarefas) + 1
        tarefa = Tarefa(id, descricao, usuario_id, categoria_id)
        self.banco.salvar('tarefas', tarefa)
        return tarefa

    def atualizar_tarefa(self, id, descricao=None):
        tarefa = self.banco.tarefas.get(id)
        if tarefa:
            tarefa.atualizar(descricao)
            self.banco.salvar('tarefas', tarefa)
            return tarefa
        return None

    def excluir_tarefa(self, id):
        self.banco.deletar('tarefas', id)

    def marcar_tarefa_concluida(self, id):
        tarefa = self.banco.tarefas.get(id)
        if tarefa:
            tarefa.marcar_como_concluida()
            self.banco.salvar('tarefas', tarefa)
            return tarefa
        return None

    def listar_tarefas_por_usuario(self, usuario_id):
        return [tarefa for tarefa in self.banco.tarefas.values() if tarefa.usuario_id == usuario_id] 