class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criado o objeto {cls.instance}')
        return cls.instance


s1 = Singleton()
print(f'Instância 1: {id(s1)}')


s2 = Singleton()
print(f'Instância 2: {id(s2)}')


"""
O método new é implementado antes do init de uma nova classe.
Dessa forma, controlamos para que seja criado somente uma instância desse objeto.
No exemplo acima mesmo sendo instanciado duas vezes, acaba apontando para o mesmo espaço na memória cls.instance
"""