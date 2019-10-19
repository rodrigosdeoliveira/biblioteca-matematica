import matematica as m

numero = int(input("informe o número "))
resposta = m.fatorial(numero)
print(resposta)

if m.primo(numero):
    print("É primo!!!")
else:
    print("Não é primo")

if m.par(numero):
    print("É par")
else:
    print("É ímpar")

print("par" if m.par(numero) else "ímpar")

print("par" if m.par2(numero) else "ímpar")

