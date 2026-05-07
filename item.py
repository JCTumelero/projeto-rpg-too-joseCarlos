import enum

class TipoItem(enum.Enum):
    ARMA = 1
    VESTIMENTA = 2
    UTILITARIO = 3

class Item:
    def __init__(self, nome, descricao, tipo, valorEfeito):
        self.__nome = nome
        self.__descricao = descricao
        self.__tipo = tipo
        self.__valorEfeito = valorEfeito

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tipo(self):
        return self.__tipo

    @property
    def valorEfeito(self):
        return self.__valorEfeito