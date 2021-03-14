def front_x(words):
    # +++ SUA SOLUÇÃO +++
    words = sorted(words)
    lista1 = []
    lista2 = []
    lista3 = []
    for palavra in words:
        if palavra[0] == 'x':
            lista1.append(palavra)
        else:
            lista2.append(palavra)
    lista3 = lista1[:] + lista2[:]

    return lista3


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
