"""
O python transforma por padrão todos módulos em um singleton
"""

import meu_modulo

print(f'O nome é {meu_modulo.NOME}')

meu_modulo.funcao1()


import meu_modulo as mm

mm.funcao2()
