import unittest
from usuario import Usuario
from tarefa import Tarefa
from banco_de_dados import BancoDeDados

class TestAceitacao(unittest.TestCase):
    def test_usuario_cria_e_conclui_tarefa(self):
        banco = BancoDeDados()
        usuario = Usuario(1, 'Maria', 'maria@email.com', 'senha123')
        usuario.cadastrar(banco)

        tarefa = Tarefa(1, 'Fazer trabalho de matemática', usuario.id, 1)
        tarefa.criar(banco)

        # Usuário marca a tarefa como concluída
        tarefa.marcar_como_concluida()
        banco.salvar('tarefas', tarefa)

        # Verifica se a tarefa está concluída
        tarefa_salva = banco.buscar('tarefas', 1)
        self.assertTrue(tarefa_salva.concluida)
        self.assertEqual(tarefa_salva.descricao, 'Fazer trabalho de matemática')
        self.assertEqual(tarefa_salva.usuario_id, usuario.id)

if __name__ == "__main__":
    unittest.main() 