import unittest
from servico_usuario import ServicoUsuario
from banco_de_dados import BancoDeDados

class TestServicoUsuario(unittest.TestCase):
    def setUp(self):
        self.banco = BancoDeDados()
        self.servico = ServicoUsuario(self.banco)

    def test_cadastrar_usuario(self):
        usuario = self.servico.cadastrar_usuario("Ana", "ana@email.com", "123")
        self.assertIn(usuario.id, self.banco.usuarios)
        self.assertEqual(usuario.nome, "Ana")

    def test_autenticar_usuario(self):
        self.servico.cadastrar_usuario("Ana", "ana@email.com", "123")
        usuario = self.servico.autenticar_usuario("ana@email.com", "123")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.email, "ana@email.com")
        self.assertIsNone(self.servico.autenticar_usuario("ana@email.com", "errada"))

    def test_atualizar_usuario(self):
        usuario = self.servico.cadastrar_usuario("Ana", "ana@email.com", "123")
        usuario2 = self.servico.atualizar_usuario(usuario.id, nome="Ana Paula")
        self.assertEqual(usuario2.nome, "Ana Paula")

    def test_excluir_usuario(self):
        usuario = self.servico.cadastrar_usuario("Ana", "ana@email.com", "123")
        self.servico.excluir_usuario(usuario.id)
        self.assertNotIn(usuario.id, self.banco.usuarios)

if __name__ == "__main__":
    unittest.main() 