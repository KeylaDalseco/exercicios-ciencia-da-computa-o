# 1 - Encontre o numero que mais se repete

nums = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1]


def count(numbers):
    count = {}
    frequent = numbers[0]

    for num in numbers:
        if num not in frequent:
            count[num] = 1
        else:
            count[num] += 1

        if count[num] > count[frequent]:
            frequent = num

    return frequent


print(count(nums))
