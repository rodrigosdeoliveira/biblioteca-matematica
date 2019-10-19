import matematica as m

numero = int(input("informe o número "))
resposta = m.fatorial(numero)
print(resposta)

if m.primo(numero):
    print("É primo!!!")
else:
    print("Não é primo")

