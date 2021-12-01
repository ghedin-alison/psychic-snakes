from abc import ABCMeta, abstractmethod


# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza_carnista(self):
        pass


# Concreto Factory_A
class PizzaBrasileira(PizzaFactory):
    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza_carnista(self):
        return PizzaStrogonoff()


# Concreto Factory_B
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaAbobrinha()

    def criar_pizza_carnista(self):
        return PizzaCalabresa()


# AbstractProductA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass


# AbstractProductB
class PizzaCarnista(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass


# ProdutoConcreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProdutoConcreto
class PizzaStrogonoff(PizzaCarnista):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com strogonoff na base de {type(PizzaVeg).__name__}')


# ProdutoConcreto
class PizzaAbobrinha(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

# Produto Concreto
class PizzaCalabresa(PizzaCarnista):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com calabresa na base de {type(PizzaVeg).__name__}')



# Cliente
class Pizzaria:
    def fazer_pizzas(self):
        for factory in[PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza_carnista = self.factory.criar_pizza_carnista()
            self.pizza_vegana = self.factory.criar_pizza_veg()
            self.pizza_vegana.preparar()
            self.pizza_carnista.servir(self.pizza_vegana)

pizzaria = Pizzaria()
pizzaria.fazer_pizzas()

