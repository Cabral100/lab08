import pytest
from senha import forca


@pytest.mark.parametrize('entrada, esperado', [
    ('abc', 'fraca'),                 # P1
    ('abcdefgh', 'media'),            # P3
    ('1abcdefg', 'media'),            # P4
    ('!abcdefg', 'media'),            # P5
    ('1234abcd', 'forte'),            # P6
])
def test_caminhos(entrada, esperado):
    assert forca(entrada) == esperado


@pytest.mark.parametrize('entrada, esperado', [
    ('', 'fraca'), ('a', 'fraca'), ('aa', 'fraca'),
    ('a' * 7, 'fraca'), ('a' * 8, 'media'), ('a' * 9, 'media'),
    ('a' * 20, 'media'), ('a' * 1000, 'media'),
    ('123abcde', 'media'), ('!!abcdef', 'forte'),
])
def test_laco_e_limiar(entrada, esperado):
    assert forca(entrada) == esperado
