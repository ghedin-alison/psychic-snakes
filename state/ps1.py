from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def manip(self):
        pass


class StateConcretA(State):

    def manip(self):
        print('StateConcretA')


class StateConcretB(State):

    def manip(self):
        print('StateConcretB')


class Context(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def manip(self):
        self.state.manip()


contexto = Context()
state_a = StateConcretA()
state_b = StateConcretB()

contexto.set_state(state_a)
contexto.manip()

contexto.set_state(state_b)
contexto.manip()

