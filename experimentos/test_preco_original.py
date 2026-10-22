import pytest
from originais_preco import preco_final


@pytest.mark.parametrize('preco, vip, esperado', [(60, True, 50), (200, False, 200)])
def test_suite_atual(preco, vip, esperado):
    assert preco_final(preco, vip) == esperado


@pytest.mark.parametrize('preco, vip, esperado', [(200, True, 160), (40, False, 50)])
def test_all_uses(preco, vip, esperado):
    assert preco_final(preco, vip) == esperado
