from abc import ABCMeta, abstractmethod


# Interface
class Carteira(metaclass=ABCMeta):

    @abstractmethod
    def pagar(self):
        pass


# Objeto Real
class Banco(Carteira):

    def __init__(self):
        self.cartao = None
        self.conta = None


    def __get_conta(self):
        self.conta = self.cartao
        return self.conta

    def __tem_saldo(self):
        print(f'Banco:: Checando se a conta {self.__get_conta()} tem saldo')
        return False

    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.__tem_saldo():
            print('Banco pagando a conta')
            return True
        else:
            print('Banco:: Desculpe, você não tem saldo suficiente')
            return False


# Proxy
class CartaoDebito(Carteira):

    def __init__(self):
        self.banco = Banco()

    def pagar(self):
        num_card = input('Proxy: Informe o numero do cartão:\n>> ')
        self.banco.set_cartao(num_card)
        return self.banco.pagar()


# Cliente
class Cliente:

    def __init__(self):
        print('Cliente:: Quero comprar uma cerveja..')
        self.cartao_debito = CartaoDebito()
        self.comprei = None

    def fazer_pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('Cliente:: Finalmente vou tomar uma cerveja!')
        else:
            print('Cliente:: Preciso aprender a fazer cerveja')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()




