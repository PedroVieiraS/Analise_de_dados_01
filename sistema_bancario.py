# 1 - criar logica que verifica o saldo de uma conta corrente
# 2 - criar segunda conta corrente, para simular saque, deposito e transferencia.
# 3 - criar um menu que permite ao usuario realizar N transações ate que el opte por sair.
import os

logado = True
banco = {
    1 : ["Pedro", "1234", 300],
    2 : ["Gabriel", "2222", 2000],
    3 : ["Heitor", "1212", 20],
}

def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')

def verificar_saldo():
    limpar_tela()
    id = int(input("Digite seu ID: "))
    print(f"Olá {banco[id][0]}, seu saldo atual é R${banco[id][2]},00")

def transferir():
    limpar_tela()
    id = int(input("Digite seu ID: "))
    print("Contas disponíveis para transferência:")
    for i in banco:
        print(f"ID: {i} - Nome: {banco[i][0]}")

    id_pessoa = int(input("Digite o ID de quem você deseja transferir: "))
    valor = int(input("Quanto você deseja transferir: R$ "))

    if banco[id][2] < valor:
        print("Saldo insuficiente para transferência!")
        return

    banco[id][2] -= valor
    banco[id_pessoa][2] += valor

    print(f"{banco[id][0]} transferiu R${valor},00 com sucesso para {banco[id_pessoa][0]}")

def sacar():
    limpar_tela()
    id = int(input("Digite seu ID: "))
    saque = int(input("Quanto você deseja sacar: R$ "))

    if banco[id][2] < saque:
        print("Saldo insuficiente!")
        return

    banco[id][2] -= saque
    print(f"Saque realizado. Saldo atual: R${banco[id][2]},00")

def depositar():
    limpar_tela()
    id = int(input("Digite seu ID: "))
    deposito = int(input("Quanto você deseja depositar: R$ "))
    banco[id][2] += deposito
    print(f"Depósito realizado. Saldo atual: R${banco[id][2]},00")

while logado:
    print("""
    ===== MENU BANCO =====
    0 - Consultar Saldo
    1 - Listar Usuários
    2 - Transferir
    3 - Sacar
    4 - Depositar
    5 - Sair
    """)
    pergunta = int(input("Escolha uma operação: "))

    match pergunta:
        case 0:
            verificar_saldo()
        case 1:
            limpar_tela()
            for i in banco:
                print(f"ID: {i} - Nome: {banco[i][0]}")
        case 2:
            transferir()
        case 3:
            sacar()
        case 4:
            depositar()
        case 5:
            logado = False
            print("Você saiu do sistema.")
