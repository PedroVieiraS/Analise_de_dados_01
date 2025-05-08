class ContaCorrente:
    def __init__(self, num_conta, senha, saldo = 0.0):
        self.num_conta = num_conta
        self.saldo = saldo
        self.senha = senha

    def consutar_saldo(self):
        print(f"O saldo da conta {self.num_conta}: R$ {self.saldo:.2f}\n")

    


    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"O saque foi realizado com sucesso! \n O saldo atual da conta: {self.saldo:.2f}\n")
        else:
            print("saldo insuficiente")

    def depositar(self, valor):
        if valor > 0: 
            self.saldo += valor
            print(f"O depoisto foi realizado com sucesso! \n O saldo atual da conta: {self.saldo:.2f}\n")
        else:
            print("Operação invalida")
        
    def transferir(self, destinatario, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            print(f"Tranferencia realizada com sucesso!\n O saldo atual é de {self.saldo:.2f}\n")
        else:    
            print("saldo insuficiente\n")
        





