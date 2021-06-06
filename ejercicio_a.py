
def es_par(numero):
    if numero % 2 == 0:
        return 'buzz'
    else:
        return False


def es_multiplo(numero):
    if numero % 5 == 0:
        return 'bazz'
    else:
        return False


if __name__ == '__main__':
    for n in range(0, 101):
        par = es_par(n)
        multiplo = es_multiplo(n)

        if par and multiplo:
            print(n, par, multiplo)
        elif par:
            print(n, par)
        elif multiplo:
            print(n, multiplo)
        else:
            print(n)
