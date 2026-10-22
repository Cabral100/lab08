"""MC/DC de causa única: pares diferem em exatamente uma condição.
Linhas numeradas de 0 a 15, com F antes de V, na ordem A, B, C, D.
"""
from itertools import combinations, product


def regra(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)


def pares_independentes(decisao, n):
    linhas = list(product((False, True), repeat=n))
    resultado = {i: [] for i in range(n)}
    for a, b in combinations(range(len(linhas)), 2):
        diferentes = [i for i in range(n) if linhas[a][i] != linhas[b][i]]
        if len(diferentes) == 1 and decisao(*linhas[a]) != decisao(*linhas[b]):
            resultado[diferentes[0]].append((a, b))
    return resultado


def conjuntos_minimos(decisao, n):
    pares = pares_independentes(decisao, n)
    for tamanho in range(n + 1, 2**n + 1):
        conjuntos = []
        for conjunto in combinations(range(2**n), tamanho):
            escolhidas = set(conjunto)
            if all(any(set(par) <= escolhidas for par in lista)
                   for lista in pares.values()):
                conjuntos.append(conjunto)
        if conjuntos:
            return conjuntos
    return []


if __name__ == "__main__":
    from originais_embarque import pode_embarcar
    linhas = list(product((False, True), repeat=4))
    for i, linha in enumerate(linhas):
        print(i, ''.join('V' if x else 'F' for x in linha),
              regra(*linha), pode_embarcar(*linha))
    print('Pares:', pares_independentes(regra, 4))
    for conjunto in conjuntos_minimos(regra, 4):
        falhas = [i for i in conjunto if pode_embarcar(*linhas[i]) != regra(*linhas[i])]
        print('Conjunto:', conjunto, 'Divergências:', falhas)
