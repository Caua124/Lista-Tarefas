from colorama import Fore, Style
import datetime

tarefas = []

def criar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data_criacao = datetime.datetime.now()
    tarefa = {"descricao": descricao, "data_criacao": data_criacao, "concluida": False}
    tarefas.append(tarefa)
    print(Fore.GREEN + "Tarefa adicionada com sucesso!" + Style.RESET_ALL)

def listar_tarefas():
    if not tarefas:
        print(Fore.RED + "Nenhuma tarefa cadastrada!" + Style.RESET_ALL)

    for tarefa in tarefas:
        print(tarefa["descricao"], tarefa["data_criacao"], tarefa["concluida"])

def concluir_tarefa():
    if not tarefas:
        print(Fore.RED + "Nenhuma tarefa cadastrada!" + Style.RESET_ALL)
    else:
        busca = input("Qual tarefa você deseja marcar como concludida? ")

    for tarefa in tarefas:
        if busca == tarefa["descricao"]:
            tarefa["concluida"] = True
            print(Fore.GREEN + "Tarefa concluida!" + Style.RESET_ALL)

def procurar_tarefa():
    if not tarefas:
        print(Fore.RED + "Nenhuma tarefa cadastrada!" + Style.RESET_ALL)
    else:
        busca = input("Digite a descrição da tarefa que deseja encontrar: ")

    for tarefa in tarefas:
        if busca == tarefa["descricao"]:
            print(Fore.GREEN + "Tarefa encontrada!" + Style.RESET_ALL)
            print(tarefa["descricao"], tarefa["data_criacao"], tarefa["concluida"])    
        else:
            print(Fore.RED + "Tarefa não encontrada!" + Style.RESET_ALL)

def remover_tarefa():
    if not tarefas:
        print(Fore.RED + "Nenhuma tarefa cadastrada!" + Style.RESET_ALL)
    else:
        busca = input("Digite a descrição da tarefa que deseja remover: ")

    for tarefa in tarefas:
        if busca == tarefa["descricao"]:
            print(Fore.GREEN + "Tarefa encontrada!" + Style.RESET_ALL)
            tarefas.remove(tarefa)
    print("Tarefa excluida com sucesso!")
    
while True:
    print(Fore.LIGHTWHITE_EX + "\n===== GERENCIADOR DE TAREFAS =====" + Style.RESET_ALL)
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Procurar tarefa")
    print("5 - Remover tarefa")
    print("0 - Sair")

    opcao = int(input("Escolha uma opcao: "))
    if opcao == 1:
        criar_tarefa()

    elif opcao == 2:
        listar_tarefas()

    elif opcao == 3:
        concluir_tarefa()

    elif opcao == 4:
        procurar_tarefa()

    elif opcao == 5:
        remover_tarefa()

    elif opcao == 0:
        print(Fore.YELLOW + "Saindo do sistema..." + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)