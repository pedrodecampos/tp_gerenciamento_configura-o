import unittest
from usuario import Usuario
from categoria import Categoria
from tarefa import Tarefa
from banco_de_dados import BancoDeDados

class TestImplementacao(unittest.TestCase):
    def test_fluxo_completo(self):
        banco = BancoDeDados()
        usuario = Usuario(1, 'João', 'joao@email.com', '123')
        categoria = Categoria(1, 'Estudos')
        tarefa = Tarefa(1, 'Estudar Python', usuario.id, categoria.id)

        # Simula salvar no banco
        banco.salvar('usuarios', usuario)
        banco.salvar('categorias', categoria)
        banco.salvar('tarefas', tarefa)

        # Busca e verifica se foi salvo corretamente
        usuario_salvo = banco.buscar('usuarios', 1)
        categoria_salva = banco.buscar('categorias', 1)
        tarefa_salva = banco.buscar('tarefas', 1)
        self.assertIsNotNone(usuario_salvo)
        self.assertIsNotNone(categoria_salva)
        self.assertIsNotNone(tarefa_salva)
        self.assertEqual(tarefa_salva.descricao, 'Estudar Python')
        self.assertFalse(tarefa_salva.concluida)

        # Marca tarefa como concluída
        tarefa_salva.marcar_como_concluida()
        self.assertTrue(tarefa_salva.concluida)

if __name__ == "__main__":
    unittest.main() 