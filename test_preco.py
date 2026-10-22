import pytest
from preco import preco_final


@pytest.mark.parametrize('preco, vip, esperado', [
    (60, True, 50), (200, False, 200),    # suíte inicial
    (200, True, 160),                    # usos de total definido no ramo VIP
    (40, False, 50),                     # uso no ramo verdadeiro, definição inicial
    (62.5, True, 50), (63, True, 50.4),   # fronteira VIP
    (50, False, 50),                     # fronteira sem desconto
])
def test_preco(preco, vip, esperado):
    assert preco_final(preco, vip) == pytest.approx(esperado)
