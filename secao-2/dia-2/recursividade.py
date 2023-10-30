def soma(number):
    if number == 0:
        return 0
    else:
        print(number)
        return number + soma(number - 1)


soma(5)

# exemplo abaixo somando os valores


def soma_recursiva_com_retorno(numero):
    if numero == 1:
        return 1
    else:
        soma = numero + soma_recursiva_com_retorno(numero - 1)
        return soma


numero = 4
resultado = soma_recursiva_com_retorno(numero)
print(f"Resultado: {resultado}")
