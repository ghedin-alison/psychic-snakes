"""
Objetivo:
organizar serviços terceirizados com sistema gerenciador de eventos
"""


class GerenciamentoEventos:
    def __init__(self):
        print("GerenciamentoEventos :: Vou organizar com todo mundo!! \n\n")

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()


# Subsistema 1
class SalaoFestas:
    def __init__(self):
        print('SalaoFestas :: Agendando o salão de festas para evento...')

    def _esta_disponivel(self):
        print('SalaFestas :: Este salao de festas está disponível? ')
        return True

    def agendar(self):
        if self._esta_disponivel():
            print('SalaFestas :: Agendamento do salao realizado. \n')


# Subsistema 2
class Florista:
    def __init__(self):
        print('Florista :: Flores para um evento..')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas e Lírios serão usados ... \n')


# Subsistema 3
class Restaurante:
    def __init__(self):
        print('Restaurante :: Comida para eventos..')

    def preparar(self):
        print('A refeição principal está sendo preparada..\n')


# Subsistema 4

class Banda:
    def __init__(self):
        print('A banda vai animar a festa')

    def montar_palco(self):
        print('A banda preparou o palco...\n')


# Cliente
class Cliente:
    def __init__(self):
        print('Cliente :: Preciso organizar um evento!')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa para gerenciar eventos\n')
        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi muito simples organizar este evento com facade..')


if __name__ == "__main__":
    cliente = Cliente()
    cliente.contrata_gerente_eventos()



