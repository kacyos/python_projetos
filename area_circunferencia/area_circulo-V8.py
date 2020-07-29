# import math
from math import pi
from termcolor import colored, cprint
import sys
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    cprint('É necessário informar o raio do círculo.', 'red')
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(colored('O raio deve ser um valor numérico', 'red'))
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo: ', area)
