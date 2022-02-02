# Exemplo Bolsa de Valores
# Criar ordens de compra e venda de ações através de um corretor
# clientes solicitam >> corretor dispara as ordens >> bolsa de valores

from abc import abstractmethod, ABCMeta


# Command
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


# Comando Concreto
class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()


class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()


# Receiver
class Acao:

    def comprar(self):
        print('Você está comprando ações')

    def vender(self):
        print('Você está vendendo ações')


# Invoker
class Agente:

    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()


if __name__ == "__main__":
    # Cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    # Chamador/Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)
