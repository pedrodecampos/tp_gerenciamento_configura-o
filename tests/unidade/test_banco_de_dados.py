import unittest
from banco_de_dados import BancoDeDados
from usuario import Usuario

class TestBancoDeDados(unittest.TestCase):
    def setUp(self):
        self.banco = BancoDeDados()
        self.usuario = Usuario(1, "João", "joao@email.com", "123")

    def test_salvar(self):
        self.banco.salvar('usuarios', self.usuario)
        self.assertIn(1, self.banco.usuarios)

    def test_buscar(self):
        self.banco.salvar('usuarios', self.usuario)
        usuario = self.banco.buscar('usuarios', 1)
        self.assertEqual(usuario.email, "joao@email.com")

    def test_deletar(self):
        self.banco.salvar('usuarios', self.usuario)
        self.banco.deletar('usuarios', 1)
        self.assertNotIn(1, self.banco.usuarios)

if __name__ == "__main__":
    unittest.main() 