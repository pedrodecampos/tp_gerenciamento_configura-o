import unittest
from validador import Validador

class TestValidador(unittest.TestCase):
    def test_validar_email(self):
        self.assertTrue(Validador.validar_email("teste@email.com"))
        self.assertFalse(Validador.validar_email("testeemail.com"))

    def test_validar_senha(self):
        self.assertTrue(Validador.validar_senha("123"))
        self.assertFalse(Validador.validar_senha("12"))

    def test_validar_descricao_tarefa(self):
        self.assertTrue(Validador.validar_descricao_tarefa("Fazer algo"))
        self.assertFalse(Validador.validar_descricao_tarefa("   "))

if __name__ == "__main__":
    unittest.main() 