#fatorial
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero*fatorial(numero-1)


#primo
def primo(numero):
    div = 0
    valor = 1
    while valor <= numero:
        if numero%valor == 0:
            div = div + 1
        valor = valor + 1
    if div == 2:
        return True
    else:
        return False

#par2
def par(numero):
    True if numero%2 == 0 else False

#potecia
def potencia_quadrada(numero):
    return numero**2

