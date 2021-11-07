"""
Lazy singleton
A instancia só é criado quando um método específico é acionado, nesse caso get_instance
"""


class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O método __init__ foi chamado..')
        else:
            print(f'A instãncia já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton() # A classe é inicializada, mas o objeto não é criado

print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton() # instância já criada...