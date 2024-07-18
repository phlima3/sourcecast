import subprocess

def run_git_command(command, return_output=False):
    try:
        if return_output:
            return subprocess.check_output(command, text=True).strip()
        else:
            subprocess.run(command, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {' '.join(command)}")
        print(e)
        exit(1)

def get_current_branch():
    return run_git_command(["git", "branch", "--show-current"], return_output=True)

def main():
    tipos_commit = [
        "feat",     # Novas funcionalidades
        "fix",      # Correções de bugs
        "docs",     # Documentação
        "style",    # Formatação, ponto e vírgula ausentes, etc; sem alteração no código
        "refactor", # Refatoração do código
        "test",     # Adicionando testes ausentes ou corrigindo testes existentes
        "chore"     # Atualizações de tarefas e pacotes, sem alteração no código
    ]
    print("Escolha um tipo de commit:")
    for i, tipo in enumerate(tipos_commit, start=1):
        print(f"{i}. {tipo}")
    
    escolha = int(input("Digite o número do tipo de commit: ")) - 1
    tipo_commit = tipos_commit[escolha]

    descricao = input("Digite a descrição do commit: ")
    mensagem_commit = f"{tipo_commit}: {descricao}"



    branch_inicial = get_current_branch()
    print(f"Branch atual: {branch_inicial}")
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", mensagem_commit])
    # run_git_command(["git", "push", "origin", branch_inicial])


if __name__ == "__main__":
    main()