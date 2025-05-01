import os
import subprocess

# Caminho do seu projeto
diretorio_projeto = r"C:\Dev\PedroVieira\analise_de_dados_1\Analise_de_dados_01"
os.chdir(diretorio_projeto)

# Loop de exerc6 até exerc50
for i in range(6, 51):
    nome = f"exerc{i}"
    nome_arquivo = f"{nome}.py"

    # Verifica se o arquivo existe antes de continuar
    if os.path.exists(nome_arquivo):
        # 1. Criar nova branch
        subprocess.run(["git", "checkout", "-b", nome], check=True)

        # 2. Adicionar o arquivo
        subprocess.run(["git", "add", nome_arquivo], check=True)

        # 3. Commitar
        subprocess.run(["git", "commit", "-m", nome], check=True)

        # 4. Voltar para main
        subprocess.run(["git", "checkout", "main"], check=True)

        print(f"Commit feito para a branch {nome}")
    else:
        print(f"Arquivo {nome_arquivo} não encontrado. Pulando...")

print("Todos os commits foram feitos.")
