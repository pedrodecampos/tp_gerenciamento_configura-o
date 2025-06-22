import unittest
from interface_console import InterfaceConsole

class TestInterfaceConsole(unittest.TestCase):
    def setUp(self):
        self.console = InterfaceConsole()

    def test_mostrar_menu(self):
        # Apenas verifica se o método pode ser chamado sem erro
        try:
            self.console.mostrar_menu()
        except Exception as e:
            self.fail(f"mostrar_menu() levantou exceção: {e}")

    def test_ler_entrada(self):
        # Não é possível testar input interativo automaticamente
        self.assertTrue(callable(self.console.ler_entrada))

    def test_exibir_mensagem(self):
        try:
            self.console.exibir_mensagem("Mensagem de teste")
        except Exception as e:
            self.fail(f"exibir_mensagem() levantou exceção: {e}")

if __name__ == "__main__":
    unittest.main() 