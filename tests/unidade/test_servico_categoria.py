import unittest
from servico_categoria import ServicoCategoria
from banco_de_dados import BancoDeDados

class TestServicoCategoria(unittest.TestCase):
    def setUp(self):
        self.banco = BancoDeDados()
        self.servico = ServicoCategoria(self.banco)

    def test_criar_categoria(self):
        categoria = self.servico.criar_categoria("Estudos")
        self.assertIn(categoria.id, self.banco.categorias)
        self.assertEqual(categoria.nome, "Estudos")

    def test_atualizar_categoria(self):
        categoria = self.servico.criar_categoria("Estudos")
        categoria2 = self.servico.atualizar_categoria(categoria.id, "Trabalho")
        self.assertEqual(categoria2.nome, "Trabalho")

    def test_excluir_categoria(self):
        categoria = self.servico.criar_categoria("Estudos")
        self.servico.excluir_categoria(categoria.id)
        self.assertNotIn(categoria.id, self.banco.categorias)

    def test_listar_tarefas_da_categoria(self):
        categoria = self.servico.criar_categoria("Estudos")
        # Não há tarefas ainda, deve retornar lista vazia
        tarefas = self.servico.listar_tarefas_da_categoria(categoria.id)
        self.assertEqual(tarefas, [])

if __name__ == "__main__":
    unittest.main() 