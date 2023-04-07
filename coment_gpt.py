import openai
import os
from unidecode import unidecode

# Insira aqui sua chave da API da OpenAI
openai.api_key = "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"

# Define o modelo de linguagem da OpenAI para português
model_engine = "text-davinci-002"

# Função para comentar o código
def comment_code(file_path):
    with open(file_path, "r+") as f:
        code = f.read()
        prompt = f"Comente o código abaixo em português:\n\n{code}"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.5,
            max_tokens=2000,
            n=1,
            stop=None,
        )
        comment = response.choices[0].text.strip()
        comment = unidecode(comment)  # Remove acentos dos comentários
        f.seek(0, 0)
        f.write(f"# Comentario: {comment}\n\n\n{code}\n\n")

# Pasta que contém os arquivos a serem processados
folder_path = "D:\\USUARIO\\Documentos\\Faculdade\\Projetos.py\\Prog-Comp-2022.2"

# Loop que processa todos os arquivos .py na pasta e subpastas
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            comment_code(file_path)
