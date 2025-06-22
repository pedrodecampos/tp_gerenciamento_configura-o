import re

class Validador:
    @staticmethod
    def validar_email(email):
        # Simples regex para validar email
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def validar_senha(senha):
        # Exemplo: senha deve ter pelo menos 3 caracteres
        return len(senha) >= 3

    @staticmethod
    def validar_descricao_tarefa(descricao):
        # Exemplo: descrição não pode ser vazia
        return bool(descricao and descricao.strip()) 