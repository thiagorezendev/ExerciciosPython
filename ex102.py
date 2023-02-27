def fatorial(n, show=False):
    """
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: O valor fatorial de um número n
    """
    print('_' * 20)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


#help(fatorial)
print(fatorial(7, True))
