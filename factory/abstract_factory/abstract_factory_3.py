from abc import ABCMeta, abstractmethod

# Abstract Factory
class CervejaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_cerveja_ale(self):
        pass

    @abstractmethod
    def criar_cerveja_lager(self):
        pass

    @abstractmethod
    def criar_cerveja_brett(self):
        pass

# ConcretoFactory 1
class CervejaInglesa(CervejaFactory):

    def criar_ceveja_ale(self):
        return CervejaIpa()

    def criar_cerveja_lager(self):
        return CervejaBalticPorter()

# ConcretoFactory 2
class CervejaAlema(CervejaFactory):

    def criar_ceveja_ale(self):
        return CervejaWeiss()

    def criar_cerveja_lager(self):
        return CervejaGermanPils()

# ConcretoFactory 3
class CervejaBelga(CervejaFactory):

    def criar_ceveja_ale(self):
        return CervejaSaison()

    def criar_cerveja_brett(self):
        return CervejaLambic()

# Abstract Product 1
class CervejaLager(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, CervejaLager):
        pass

# Abstract Product 1
class CervejaAle(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, CervejaAle):
        pass

# Abstract Product 1
class CervejaLambic(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, CervejaAle):
        pass

# Produto concreto
class CervejaIpa(CervejaAle):

    def preparar(self, CervejaLager):
        print(f'{type(self).__name__} pode ter uma base de {type(CervejaLager).__name__} com adição de levedura Ale')


# Produto concreto
class CervejaBalticPorter(CervejaLager):

    def preparar(self):
        print(f'{type(self).__name__} é preparada usando levedura Lager')


# Produto concreto
class CervejaWeiss(CervejaAle):

    def preparar(self, CervejaLager):
        print(f'{type(self).__name__} pode ter uma base de {type(CervejaLager).__name__} com adição de levedura Ale')


# Produto concreto
class CervejaGermanPils(CervejaLager):

    def preparar(self):
        print(f'{type(self).__name__} é preparada usando levedura Lager')


# Produto concreto
class CervejaSaison(CervejaAle):

    def preparar(self):
        print(f'{type(self).__name__} é preparada usando levedura Ale')

# Produto concreto
class CervejaLambic(CervejaAle):

    def preparar(self, CervejaLambic):
        print(f'{type(self).__name__} é preparada adicionando levedura lambic')


class Cervejaria:
    def produzir(self):
        for factory in[CervejaInglesa(), CervejaAlema(), CervejaBelga()]:
            self.factory = factory
            self.lager = self.factory.criar_cerveja_lager()
            self.ale = self.factory.criar_cerveja_ale()
            self.lager.preparar()
            self.ale.preparar(self.lager)

cervejaria = Cervejaria()
cervejaria.produzir()
