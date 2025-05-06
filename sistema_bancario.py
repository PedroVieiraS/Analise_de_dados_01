# 1 - criar logica que verifica o saldo de uma conta corrente
# 2 - criar segunda conta corrente, para simular saque, deposito e transferencia.
# 3 - criar um menu que permite ao usuario realizar N transações ate que el opte por sair.
logado = True
banco = {
    1 : ["Pedro", "1234", 300],
    2 : ["Gabriel", "2222", 2000],
    3 : ["Heitor", "1212", 20],
}

def verificar_saldo():
    id = int(input("digite seu id:"))
    print(f"Ola {banco[id][0]}, seu saldo atual é R${banco[id][2]},00")



while(logado):


    print("""
    menu: 
    0 - consultar saldo
    1 - digite para sair
    """)
    pergunta = int(input("digite um numero"))

    if pergunta == 1:
        logado = False
    elif pergunta == 0:    
        verificar_saldo()




