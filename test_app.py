"""Testes unitários
"""

import mock

import app

def test_lambda_comparar_nok():
    """Teste: lambda "comparar"
"""

    assert not app.comparar("x", "y")

def test_lambda_comparar_ok():
    """Teste: lambda "comparar"
"""

    assert app.comparar("x", "x")

def test_lambda_inicializar_ok():
    """Teste: lambda "inicializar"
"""

    termo = "teste"

    termo_esperado = {

        0: {"char": "t", "peso": -1},
        1: {"char": "e", "peso": -1},
        2: {"char": "s", "peso": -1},
        3: {"char": "t", "peso": -1},
        4: {"char": "e", "peso": -1}
    }

    termo_inicializado = app.inicializar(termo)

    assert termo_inicializado == termo_esperado

def test_obter_termo():
    """Teste: função "obter_termo"
"""

    lista = [ "teste", "ações" ]

    termo = app.obter_termo(lista)

    assert termo in lista

def test_validar_entrada_nao_eh_lista():
    """Teste: função "validar_entrada"
"""

    termo = "teste"
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_lista_vazia():
    """Teste: função "validar_entrada"
"""

    termo = []
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_nao_alfabetica():
    """Teste: função "validar_entrada"
"""

    termo = [ "test1" ]
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_menos_5_letras():
    """Teste: função "validar_entrada"
"""

    termo = [ "test" ]
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_mais_5_letras():
    """Teste: função "validar_entrada"
"""

    termo = [ "testes" ]
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_vazia():
    """Teste: função "validar_entrada"
"""

    termo = [ "" ]
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_fora_da_lista():
    """Teste: função "validar_entrada"
"""

    termo = [ "abcde" ]
    lista = [ "teste", "ações" ]

    assert not app.validar_entrada(termo, lista)

def test_validar_entrada_ok():
    """Teste: função "validar_entrada"
"""

    termo = [ "teste" ]
    lista = [ "teste", "ações" ]

    assert app.validar_entrada(termo, lista)

def test_validar_entrada_com_acentuacao_ok():
    """Teste: função "validar_entrada"
"""

    termo = [ "acoes" ]
    lista = [ "teste", "ações" ]

    termo_esperado = [ "ações" ]

    app.validar_entrada(termo, lista)

    assert termo == termo_esperado

def somar_pesos(termo):
    """Função "somar_pesos"
"""

    return sum( val["peso"] for chv, val in termo.items() )

def test_atribuir_pesos_errados():
    """Teste: função "atribuir_pesos"
"""

    gabarito = app.inicializar("teste")

    termo = app.inicializar("balao")

    app.atribuir_pesos(termo, gabarito)

    assert somar_pesos(termo) == 0

def test_atribuir_pesos_quase_certos():
    """Teste: função "atribuir_pesos"
"""

    gabarito = app.inicializar("odiar")

    termo = app.inicializar("radio")

    app.atribuir_pesos(termo, gabarito)

    assert somar_pesos(termo) == 5

def test_atribuir_pesos_certos():
    """Teste: função "atribuir_pesos"
"""

    gabarito = app.inicializar("teste")

    termo = app.inicializar("teste")

    app.atribuir_pesos(termo, gabarito)

    assert somar_pesos(termo) == 10

def test_validar_termo_nok():
    """Teste: função "validar_termo"
"""

    gabarito = app.inicializar("odiar")

    termo = app.inicializar("radio")

    app.atribuir_pesos(termo, gabarito)

    assert not app.validar_termo(termo)

def test_validar_termo_ok():
    """Teste: função "validar_termo"
"""

    gabarito = app.inicializar("teste")

    termo = app.inicializar("teste")

    app.atribuir_pesos(termo, gabarito)

    assert app.validar_termo(termo)

def test_main_entrada_nok():
    """Teste: função "main"
"""

    termos = ["turma", "acoes", "adiar", "saldo", "radio"]

    entrada = ["abcde", "turma", "acoes", "adiar", "saldo", "radio"]

    with mock.patch('random.choice', return_value = "teste"):
        with mock.patch("builtins.input", side_effect = entrada):

            assert not app.main(termos)

def test_main_game_over():
    """Teste: função "main"
"""

    termos = ["teste", "acoes", "adiar", "saldo", "radio"]

    with mock.patch('random.choice', return_value = "testa"):
        with mock.patch("builtins.input", return_value = "teste"):

            assert not app.main(termos)

def test_main_ok():
    """Teste: função "main"
"""

    termos = ["teste", "acoes", "adiar", "saldo", "radio"]

    with mock.patch('random.choice', return_value = "teste"):
        with mock.patch("builtins.input", return_value = "teste"):

            assert app.main(termos)
