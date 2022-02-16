from abc import ABCMeta, abstractmethod

class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    # método template implementado aqui, é um exemplo de hook. podemos implementar outros métodos(hooks)com
    # particularidades que se façam necessárias.
    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print("Viagem de avião")

    def dia1(self):
        print("Visita a praça São Marcos")

    def dia2(self):
        print("Andar de gondola")

    def dia3(self):
        print("Aproveitar a culinária local")

    def retorno(self):
        print("Viagem de aviao...")


class ViagemMalvinas(Viagem):

    def ida(self):
        print("Viagem de Ônibus")

    def dia1(self):
        print("Apreciar a vida marinha")

    def dia2(self):
        print("Praticar esportes aquaticos")

    def dia3(self):
        print("Relaxar na praia e aproveitar o sol")

    def retorno(self):
        print("Viagem de aviao...")

class GeekTravel:
    def preparar_viagem(self):
        opcao = input("Escolha o pacote de viagem: [Veneza, Malvinas]\n")

        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == "Malvinas":
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print("Opção inválida!!")


agencia = GeekTravel()
agencia.preparar_viagem()


