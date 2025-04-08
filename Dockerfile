# Usa uma imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5000

# Define o comando padrão para rodar o app
CMD ["python", "todo_project/run.py"]







