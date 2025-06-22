# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . /app

# Instala dependências, se houver requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando padrão para rodar o app
CMD ["python", "app.py"] 