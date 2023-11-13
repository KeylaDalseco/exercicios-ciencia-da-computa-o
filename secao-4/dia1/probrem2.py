# 1 - interseção entre listas - numeros que se repetem

lista = [1, 2, 3, 4]
listab = [5, 6, 2, 1]


def intersection(listA, listB):
    inA = {}

    for item in listA:
        if item not in inA:
            inA[item] = True

    ans = []
    for item in listB:
        if item in inA:
            ans.append(item)
    return ans


print(intersection(lista, listab))
