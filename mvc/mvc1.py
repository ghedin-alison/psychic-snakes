class Modelo:
    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': 1244},
            'ps5': {'id': 2, 'nome': 'Xbox 360', 'preco': 1445},
            'ps5': {'id': 3, 'nome': 'Nintendo Wii', 'preco': 1567}
        }


class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('-' * 10 + ' Produtos' + '-' * 10)
        for chave in produtos:
            print(f"ID: {self.modelo.produtos[chave]['id']}")
            print(f"Nome: {self.modelo.produtos[chave]['nome']}")
            print(f"Preco: {self.modelo.produtos[chave]['preco']}")
            print('')


class Visao:

    def __init__(self):
        self.controlador = Controlador()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == "__main__":
    visao = Visao()
    visao.produtos()
