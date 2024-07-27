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
    tipos_commit = {
        "feat": "Nova funcionalidade",
        "fix": "Correção de bug",
        "docs": "Atualização da documentação",
        "style": "Melhorias de formatação (sem mudanças no código)",
        "refactor": "Refatoração de código (sem mudanças na funcionalidade)",
        "test": "Adição ou correção de testes",
        "chore": "Atualização de build ou mudanças que não afetam o código"
    }

    print("Escolha um tipo de commit:")
    for i, (tipo, descricao) in enumerate(tipos_commit.items(), start=1):
        print(f"{i}. {tipo}: {descricao}")

    # Validação da escolha do tipo de commit
    while True:
        try:
            escolha = int(input("Digite o número do tipo de commit: ")) - 1
            if 0 <= escolha < len(tipos_commit):
                tipo_commit = list(tipos_commit.keys())[escolha]
                break
            else:
                print("Escolha inválida. Digite um número entre 1 e", len(tipos_commit))
        except ValueError:
            print("Entrada inválida. Digite um número.")

    descricao = input("Digite a descrição do commit: ")
    mensagem_commit = f"{tipo_commit}: {descricao}"

    branch_inicial = get_current_branch()
    print(f"Branch atual: {branch_inicial}")
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", mensagem_commit])

    # Confirmação antes do push
    confirmar_push = input("Deseja enviar as alterações para o repositório remoto? (s/n): ")
    if confirmar_push.lower() == "s":
        run_git_command(["git", "push", "origin", branch_inicial])
    else:
        print("Push cancelado.")


if __name__ == "__main__":
    main()
