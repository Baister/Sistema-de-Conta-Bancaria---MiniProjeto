#Criando mini projeto - com Classe kkkk
import os
def limpa_tela():
    os.system('cls')

class Conta():
    def __init__(self,banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0 #Colocando valor Default

    def depositar(self,deposito):
        if deposito <= 0:
            raise ValueError("Favor fazer um depósito maior que 0!")
        
        self.saldo += deposito

    def sacar(self,sacado):
        if self.saldo < sacado:
            raise ValueError("Saldo insuficiente para saque!")
        
        if sacado <= 0:
            raise ValueError("Favor fazer um saque maior que 0!")
        self.saldo -= sacado

    def __str__(self):
        return (f'Agência: {self.agencia}\n'
                f'Conta: {self.conta}\n'
                f'Saldo: R${self.saldo:.2f}')

limpa_tela()
conta_PagBank = Conta('PagBank', '3219','42931')
conta_PagBank.depositar(400)
conta_PagBank.sacar(300)
print(conta_PagBank)