# 1 - separe as palavras de acordo com a letra inicial

text = ['Ana', 'ana', 'Joao', 'que', 'nao', 'Jose']


def screening(text):
    screnn = {}

    for word in text:
        first_char = word[0]
        if first_char not in screnn:
            screnn[first_char] = [word]
        else:
            screnn[first_char].append(word)


for key, value in screening(text):
    print(f"{key}: {value}")
