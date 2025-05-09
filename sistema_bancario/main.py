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
        senha = input("digite sua senha")
        
        conta = contas.get(num_conta)
        
        if conta and conta.senha == senha:
            print(f"Seja bem-vindo(a), {conta.num_conta}")
            return conta
        else:
            print("login invalido")
            login()

conta_logada = login()

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
            conta_logada.consutar_saldo()
        case 1:
            limpar_tela()
            # for i in contas:
            #    print(f"Nome: {contas[i]}")
        case 2:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            num_conta_destino = input("Digite a conta do destinatario: ")

            if num_conta_destino in contas and num_conta_destino != conta_logada.num_conta:
                conta_logada.transferir(contas[num_conta_destino],valor)
            else:
                print("Conta destino não encontrada")
        case 3:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            conta_logada.sacar(valor)
        case 4:
            limpar_tela()
            valor =  float(input("Escolha o valor"))
            conta_logada.depositar(valor)
        case 5:
            logado = False
            print("Você saiu do sistema.")
        case _:
            print("Opção invalida")


