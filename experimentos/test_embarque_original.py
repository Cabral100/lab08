from itertools import product
import pytest
from originais_embarque import pode_embarcar
from mcdc import regra, conjuntos_minimos

LINHAS = list(product((False, True), repeat=4))


@pytest.mark.parametrize('entrada', [(True,) * 4, (False,) * 4])
def test_extremos(entrada):
    assert pode_embarcar(*entrada) == regra(*entrada)


@pytest.mark.parametrize('conjunto', conjuntos_minimos(regra, 4))
def test_mcdc(conjunto):
    for i in conjunto:
        assert pode_embarcar(*LINHAS[i]) == regra(*LINHAS[i])
