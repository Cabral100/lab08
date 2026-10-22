def preco_final(preco, vip):
    total = preco
    if vip:
        total = total * 0.8
    if total < 50:
        total = 50
    return total
