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

def main(mensagem_commit):
    branch_inicial = get_current_branch()
    print(f"Branch atual: {branch_inicial}")
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", mensagem_commit])
    run_git_command(["git", "push", "origin", branch_inicial])


if __name__ == "__main__":
    mensagem_commit = input("Digite a mensagem de commit: ")
    main(mensagem_commit)