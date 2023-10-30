# como visualizar informações de uma instancia do objeto:

class Pet():
    def __init__(self, nome, especie, idade, humano):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.humano = humano

    def __str__(self):
        return f"""
        - Espécie do pet: {self.especie}
        - Nome do pet: {self.nome}
        - Idade do pet: {self.idade}
        - Pessoa do pet: {self.humano}
        """


thor = Pet('thor', 'gato', 5, 'keyla')
print(thor)
# retorna um objeto pet, que está na main e nessa posição
# de memória -> retorno <__main__.Pet object at 0x7f6292b57f40>
