# EXERCÍCIO 1


def maiorNumero(num1, num2):
    if num1 > num2:
        return num1
    return num2


# EXERCÍCIO 2
numbers = [1, 2, 3, 4, 5]


def media(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

# EXERCÍCIO 3


def quadrado(n):
    for row in range(n):
        print(n * '*')

# *****
# *****
# *****

# EXERCÍCIO 4


names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def lenght(names):
    maiorNome = names[0]
    for name in names:
        if len(names) > len(maiorNome):
            maiorNome = name
    return maiorNome

# EXERCICIO 5


def type_of_triangle(side1, side2, side3):
    is_triangle = (
            side1 + side2 > side3 and
            side2 + side3 > side1 and
            side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"


# EXERCICIO 6


numbers2 = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]


def minimumNumber(numbers):
    menorNumero = numbers[0]
    for number in numbers:
        if number < menorNumero:
            menorNumero = number
    return menorNumero

# OU


def minimum(numbers):
    return min(numbers)


# EXERCICIO 7


def triangulo(n):
    for row in range(1, n + 1):
        print(row * '*')

# *
# **
# ***
# ****
# *****
