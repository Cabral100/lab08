from itertools import product
import pytest
from embarque import pode_embarcar
from mcdc import regra, pares_independentes, conjuntos_minimos

LINHAS = list(product((False, True), repeat=4))
CONJUNTOS = conjuntos_minimos(regra, 4)


@pytest.mark.parametrize('entrada', [(True,) * 4, (False,) * 4])
def test_extremos(entrada):
    assert pode_embarcar(*entrada) == regra(*entrada)


@pytest.mark.parametrize('conjunto', CONJUNTOS)
def test_mcdc(conjunto):
    for i in conjunto:
        assert pode_embarcar(*LINHAS[i]) == regra(*LINHAS[i])


@pytest.mark.parametrize('entrada', LINHAS)
def test_mcc(entrada):
    assert pode_embarcar(*entrada) == regra(*entrada)


def test_enumeracao_mcdc():
    assert [len(p) for p in pares_independentes(regra, 4).values()] == [3, 3, 1, 1]
    assert len(CONJUNTOS) == 4
    assert all(len(c) == 5 for c in CONJUNTOS)
