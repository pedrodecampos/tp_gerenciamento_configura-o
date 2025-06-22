# Sistema de Gerenciamento de Tarefas

Este projeto é um sistema simples de gerenciamento de tarefas, desenvolvido em Python, com arquitetura modular, testes automatizados e pipeline de CI/CD.

## Objetivo

Permitir o cadastro de usuários, criação e gerenciamento de tarefas, organização por categorias e marcação de tarefas como concluídas, tudo via terminal.

## Estrutura do Projeto

```
├── app.py                  # Ponto de entrada do sistema
├── usuario.py              # Classe Usuario
├── tarefa.py               # Classe Tarefa
├── categoria.py            # Classe Categoria
├── banco_de_dados.py       # Simulação de persistência
├── servico_usuario.py      # Lógica de usuário
├── servico_tarefa.py       # Lógica de tarefa
├── servico_categoria.py    # Lógica de categoria
├── validador.py            # Validações
├── interface_console.py    # Interação via terminal
├── requirements.txt        # Dependências do projeto
├── Dockerfile              # Containerização do sistema
├── tests/                  # Testes automatizados
│   ├── unidade/            # Testes de unidade
│   ├── integracao/         # Testes de integração
│   └── aceitacao/          # Testes de aceitação
└── .github/workflows/ci-cd.yml # Pipeline CI/CD (GitHub Actions)
```

## Como Executar

### Localmente

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```
2. **Execute o sistema:**
   ```bash
   python3 app.py
   ```

### Com Docker

1. **Build da imagem:**
   ```bash
   docker build -t meu-projeto-tarefas .
   ```
2. **Execute o container:**
   ```bash
   docker run -it meu-projeto-tarefas
   ```

## Como Rodar os Testes

- Todos os testes:
  ```bash
  python3 -m unittest discover tests
  ```
- Testes de unidade:
  ```bash
  python3 -m unittest discover tests/unidade
  ```
- Testes de integração:
  ```bash
  python3 -m unittest discover tests/integracao
  ```
- Testes de aceitação:
  ```bash
  python3 -m unittest discover tests/aceitacao
  ```

## CI/CD

O projeto possui pipeline automatizado com **GitHub Actions**:

- Roda todos os testes a cada commit/pull request na branch principal.
- Faz build da imagem Docker.
- Arquivo de configuração: `.github/workflows/ci-cd.yml`

## Licença

Este projeto é livre para fins acadêmicos e de estudo.
