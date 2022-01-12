class Objeto:

    def __init__(self):
        self.observadores = []

    def __repr__(self):
        return '::Telegram::'

    def registrar(self, observador):
        self.observadores.append(observador)

    def notificar_todos(self, *args, **kwargs):
        for observador in self.observadores:
            observador.notificar(self, *args, **kwargs)


class ObservadorA:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {objeto}')


class ObservadorB:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {objeto}')


obj = Objeto()

obj_a = ObservadorA(obj)
obj_b = ObservadorB(obj)

obj.notificar_todos('notificação')