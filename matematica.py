#fatorial
def fatorial(numero):
    fat = 1
    while numero > 0:
        fat = fat * numero
        numero = numero - 1
    return fat


#primo
def primo(numero):
    div = 0
    valor = 1
    while valor <= numero:
        if numero%valor == 0:
            div = div + 1
        valor = valor + 1
    if div == 2:
        print("É primo")
    else:
        print("Não é primo")