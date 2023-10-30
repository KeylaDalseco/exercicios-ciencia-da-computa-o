# CRIE A CLASSE TV COM OS METODOS DO DIAGRAMA

class TV:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if canal < 1 or canal > 99:
            raise ValueError("Canal inválido")
        self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada


tv = TV(32)
print(tv._TV__volume)
tv.aumentar_volume()
print(tv._TV__volume)
tv.modificar_canal(5)
tv.ligar_desligar()
