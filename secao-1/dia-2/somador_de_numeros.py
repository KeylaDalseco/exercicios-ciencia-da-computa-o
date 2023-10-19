# Todo input retorna uma string
# Devemos converter para número com int

meu_numero = 0

while meu_numero < 42:
    meu_numero += int(input("Digite seu número:"))


print("A soma dos números superou 42")

# Como colocar o nome letra por letra

name = input("Qual o seu nome?")


for carac in name:
    print(carac)


# programa que receba vários números naturais e calcule a soma desses valores
# se não for número exiba uma mensagem


nums = input("Insira valores aqui, separados por espaço: ")

nums_arr = nums.split(" ")

sum = 0
for num in nums_arr:
    if not num.isdigit():
        print(f"Erro ao somar valores, {num} não é um dígito.")
    else:
        sum += int(num)

print(f"A soma dos valores válidos é: {sum}")


# DESENPACOTAMENTO DE VALORES

a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = (1, 2, 3)  # Quando um * está presente no desempacotamento,
# os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]
