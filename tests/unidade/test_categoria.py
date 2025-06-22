import unittest
from categoria import Categoria
from tarefa import Tarefa
from banco_de_dados import BancoDeDados

class TestCategoria(unittest.TestCase):
    def setUp(self):
        self.banco = BancoDeDados()
        self.categoria = Categoria(1, "Estudos")
        self.categoria.criar(self.banco)
        self.tarefa = Tarefa(1, "Ler livro", 1, 1)
        self.tarefa.criar(self.banco)

    def test_criar(self):
        self.assertIn(1, self.banco.categorias)

    def test_atualizar(self):
        self.categoria.atualizar("Trabalho")
        self.assertEqual(self.categoria.nome, "Trabalho")

    def test_excluir(self):
        self.categoria.excluir(self.banco)
        self.assertNotIn(1, self.banco.categorias)

    def test_listar_tarefas(self):
        tarefas = Categoria.listar_tarefas(self.banco, 1)
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0].descricao, "Ler livro")

if __name__ == "__main__":
    unittest.main() 