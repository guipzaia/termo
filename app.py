"""Game baseado no Wordle
"""

import random
from unidecode import unidecode
from termcolor import colored

import constants

# Compara duas strings
comparar = lambda c1, c2: unidecode(c1.lower()) == unidecode(c2.lower())

# Inicializa um termo com pesos vazios
inicializar = lambda str: { ind: {"char": val, "peso": constants.NRO_PESO_VAZIO}
                            for ind, val in enumerate( list(str) ) }

def obter_termo(lista):
    """Obter termo aleatório a partir de uma lista.
"""

    random.seed()

    return random.choice(lista)

def validar_entrada(termo, lista):
    """Verifica se termo informado é valido.
Deve ser uma palavra com 5 letras e estar contido na lista.
"""

    if isinstance(termo, list) and len(termo) > 0 and \
        len(termo[0]) == 5 and unidecode(termo[0]).isalpha():

        for item in lista:

            if comparar(termo[0], item):

                termo[0] = item

                return True

    return False

def atribuir_pesos(termo, gabarito):
    """Atribui pesos conforme cada letra do termo informado está de acordo com o gabarito.
0 - Gabarito não possui letra;
1 - Gabarito posui letra, mas está fora de ordem;
2 - Gabarito possui letra e está na ordem correta.
"""

    for t_chv, t_val in termo.items():

        if comparar(t_val["char"], gabarito[t_chv]["char"]):

            t_val["peso"] = constants.NRO_PESO_CERTO
            gabarito[t_chv]["peso"] = constants.NRO_PESO_CERTO

    for t_chv, t_val in termo.items():

        if t_val["peso"] == constants.NRO_PESO_VAZIO:

            for __, g_val in gabarito.items():

                if g_val["peso"] == constants.NRO_PESO_VAZIO:

                    if  comparar(g_val["char"], t_val["char"]):

                        t_val["peso"] = constants.NRO_PESO_QUASE_CERTO
                        g_val["peso"] = constants.NRO_PESO_QUASE_CERTO

                        break
            else:
                t_val["peso"] = constants.NRO_PESO_ERRADO

def validar_termo(termo):
    """Valida termo informado.
Termo está correto se a soma dos pesos for igual a 10.
"""

    return sum( val["peso"] for __, val in termo.items() ) == (5 * constants.NRO_PESO_CERTO)

def imprimir(termo):
    """Imprime termo em tela, colorindo as letras de acordo com os pesos.
"""

    for __, val in termo.items():

        print( colored( val["char"].upper(), constants.CORES[ val["peso"] ] ), end = " " )

    print()

def main(lista):
    """Função main.
Compõe a lógica do game.
"""

    termo_gabarito = obter_termo(lista)

    for __ in range(constants.NRO_TENTATIVAS):

        gabarito = inicializar(termo_gabarito)

        while True:

            termo_informado = [ input() ]

            if validar_entrada(termo_informado, lista):
                break

            print(constants.MSG_TERMO_INVALIDO)

        termo = inicializar(termo_informado[0])

        atribuir_pesos(termo, gabarito)

        imprimir(termo)

        if validar_termo(termo):
            return True

    imprimir(termo)

    return False

if __name__ == '__main__': # pragma: no cover

    with open("termos.txt", "r", encoding = "utf-8") as arq:

        termos = arq.read().splitlines() or []

        main(termos)
