class BancoDeDados:
    def __init__(self):
        self.usuarios = {}
        self.tarefas = {}
        self.categorias = {}

    def salvar(self, tipo, obj):
        if tipo == 'usuarios':
            self.usuarios[obj.id] = obj
        elif tipo == 'tarefas':
            self.tarefas[obj.id] = obj
        elif tipo == 'categorias':
            self.categorias[obj.id] = obj

    def buscar(self, tipo, id):
        if tipo == 'usuarios':
            return self.usuarios.get(id)
        elif tipo == 'tarefas':
            return self.tarefas.get(id)
        elif tipo == 'categorias':
            return self.categorias.get(id)

    def deletar(self, tipo, id):
        if tipo == 'usuarios':
            self.usuarios.pop(id, None)
        elif tipo == 'tarefas':
            self.tarefas.pop(id, None)
        elif tipo == 'categorias':
            self.categorias.pop(id, None) 