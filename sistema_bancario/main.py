from conta import ContaCorrente
import os


logado = True


contas = {
    "1234-5" : ContaCorrente("1234-5","123", 100.0),
    "5432-1" : ContaCorrente("5432-1","123", 2000.0)
}

def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')

def login():
        num_conta = input("digite sua conta")
        senha = input("digite sua conta")
        
        conta = contas.get(num_conta)
        
        if conta and conta.senha == senha:
            print(f"Seja bem-vindo(a), {conta.num_conta}")


while logado:
    print("""
    ===== MENU BANCO =====
    0 - Consultar Saldo
    1 - Listar Usuários - com defeito
    2 - Transferir
    3 - Sacar
    4 - Depositar
    5 - Sair
    """)
    pergunta = int(input("Escolha uma operação: "))

    match pergunta:
        case 0:
            contas["1234-5"].consutar_saldo()
        case 1:
            limpar_tela()
            # for i in contas:
            #    print(f"Nome: {contas[i]}")
        case 2:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            conta1.transferir(conta2,valor)
        case 3:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            conta1.sacar(valor)
        case 4:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            conta1.depositar(valor)
        case 5:
            logado = False
            print("Você saiu do sistema.")
        case _:
            print("Opção invalida")


