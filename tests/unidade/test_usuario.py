import unittest
from usuario import Usuario
from banco_de_dados import BancoDeDados

class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.banco = BancoDeDados()
        self.usuario = Usuario(1, "João", "joao@email.com", "123")

    def test_cadastrar(self):
        self.usuario.cadastrar(self.banco)
        self.assertIn(1, self.banco.usuarios)

    def test_autenticar(self):
        self.assertTrue(self.usuario.autenticar("123"))
        self.assertFalse(self.usuario.autenticar("errada"))

    def test_atualizar(self):
        self.usuario.atualizar(nome="Maria", email="maria@email.com", senha="456")
        self.assertEqual(self.usuario.nome, "Maria")
        self.assertEqual(self.usuario.email, "maria@email.com")
        self.assertEqual(self.usuario.senha, "456")

    def test_excluir(self):
        self.usuario.cadastrar(self.banco)
        self.usuario.excluir(self.banco)
        self.assertNotIn(1, self.banco.usuarios)

if __name__ == "__main__":
    unittest.main() 